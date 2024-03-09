"""VietFin helper functions."""

from typing import Iterable, Any, Sequence, Literal
from typing_extensions import Annotated
import re
import ast
from datetime import datetime, timezone, timedelta

import pandas as pd
from pydantic.functional_validators import AfterValidator
from pydantic import BaseModel, field_validator, model_validator
import requests

from vietfin.abstract.data import Data


def to_snake_case(string: str) -> str:
    """Convert a string to snake case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    return (
        re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        .lower()
        .replace(" ", "_")
        .replace("__", "_")
    )


def datetime_ge_1970(v: datetime) -> datetime:
    """Enforce datetime >= 1970-01-01.

    Return None if date before 1970-01-01.

    """
    # Create a reference datetime for comparison (offset-aware or offset-naive based on input)
    reference_date = datetime(1970, 1, 1, 0, 0)
    if v.tzinfo is not None and v.tzinfo.utcoffset(v) is not None:
        reference_date = reference_date.replace(tzinfo=timezone.utc)

    # Compare to the appropriate type of datetime
    if v < reference_date:
        return None  # type: ignore
    return v


# Custom type created via Pydantic Annotated validator for datetime data type
ValidatedDatetime = Annotated[datetime, AfterValidator(datetime_ge_1970)]


def basemodel_to_df(
    data: list[Data] | Data,
    index: str | Iterable | None = None,
) -> pd.DataFrame:
    """Convert a list of Pydantic BaseModel to a Pandas DataFrame.

    source: https://github.com/OpenBB-finance/OpenBBTerminal/blob/develop/openbb_platform/core/openbb_core/app/utils.py
    """
    if isinstance(data, list):
        df = pd.DataFrame([d.model_dump() for d in data])
    else:
        try:
            df = pd.DataFrame(data.model_dump())
        except ValueError:
            df = pd.DataFrame(data.model_dump(), index=["values"])

    if "is_multiindex" in df.columns:
        col_names = ast.literal_eval(df.multiindex_names.unique()[0])
        df = df.set_index(col_names)
        df = df.drop(["is_multiindex", "multiindex_names"], axis=1)

    if index and index in df.columns:
        df = df.set_index(index)  # type: ignore
        # TODO: This should probably check if the index can be converted to a datetime instead of just assuming
        if df.index.name == "date":
            df.index = pd.to_datetime(df.index)
            df.sort_index(axis=0, inplace=True)

    return df


def generate_extra_metadata(
    symbol: str | None = None,
    result: Sequence[Data] | None = None,
    api_url: str | list[str] | None = None,
) -> dict:
    """Generate extra metadata for VfObject.

    Parameters
    ----------
    symbol : str
        the symbol for which the command is run, by default None
    result : Sequence[Data]
        the result of the command, by default None
    api_url : str | list[str]
        the API url(s) used by the command, by default None

    Returns
    -------
    metadata : dict
        extra metadata for VfObject
            command_run_at : str
                The datetime at which the command was executed.
            symbol : str
                The symbol for which the command is run.
            records_count : int
                The number of records returned by the command.
            api_url : str | list[str]
                The API url(s) called by the command.
    """
    metadata: dict[str, Any] = {
        "command_run_at": datetime.now(timezone.utc).isoformat()
    }

    if symbol is not None:
        metadata["symbol"] = symbol

    if result is not None:
        metadata["records_count"] = len(result)

    if api_url is not None:
        metadata["api_url"] = api_url

    return metadata


def check_response_error(response: requests.Response) -> None:
    """Check the HTTP response and raise an exception if there are any errors.

    Parameters
    ----------
    response : requests.Response
        The HTTP response to check.

    Raises
    ------
    requests.exceptions.HTTPError
        If the response status code indicates an error.
    """

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error in API response: {response.status_code} - {response.text}"
        )


def convert_dictlists_to_listdicts(data: dict) -> list:
    """Transpose a dictionary of lists into a list of dictionaries.

    Parameters
    ----------
    data : dict
        A dictionary where values are lists of equal length.

    Returns
    -------
    list
        A list of dictionaries, where each dictionary represents a row of the transposed data.
    """
    return [
        dict(zip(data.keys(), t))
        for t in zip(*[v for v in data.values() if isinstance(v, list)])
    ]


class BaseDateParams(BaseModel):
    """Base class to validate date params in function.

    Base validation rules:
    - start_date and end_date must be a string in YYYY-MM-DD format
    - set default end_date to the current date, if not provided
    - set default start_date to 60 days before end_date, if not provided
    - start_date must be < end_date
    - end_date must be <= today
    """

    start_date: str | None = None
    end_date: str | None = None

    @field_validator("start_date", "end_date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        """Enforce date string format as YYYY-MM-DD."""

        # if date is None or an empty string "", return as is
        if v is None or v == "":
            return v

        # Enforce the date string format as YYYY-MM-DD
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date: {v}. Date format is YYYY-MM-DD.")
        return v

    @model_validator(mode="before")
    @classmethod
    def set_default_end_date(cls, data: Any) -> Any:
        """Before validation, set default end_date to current date, if not provided."""

        current_date = datetime.now()

        if (
            "end_date" not in data
            or data["end_date"] is None
            or data["end_date"] == ""
        ):
            data["end_date"] = current_date.strftime("%Y-%m-%d")
            print(f"end_date not provided, set to {data.get('end_date')}")

        return data

    @model_validator(mode="after")
    def set_default_start_date(self) -> "BaseDateParams":
        """Set default start_date to 60 days before end_date, if not provided."""

        s = self.start_date
        end_dt = datetime.strptime(self.end_date, "%Y-%m-%d")  # type: ignore

        if s is None or s == "":
            self.start_date = (end_dt - timedelta(days=60)).strftime("%Y-%m-%d")
            print(f"start_date not provided, set to {self.start_date}")

        return self

    @model_validator(mode="after")
    def check_date_range(self) -> "BaseDateParams":
        """Enforce start_date < end_date."""

        if self.start_date and self.end_date:
            start_dt = datetime.strptime(self.start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(self.end_date, "%Y-%m-%d")

            if start_dt > end_dt:
                print(
                    f"The start_date {self.start_date} is after end_date {self.end_date}. Swapped dates."
                )
                self.start_date, self.end_date = self.end_date, self.start_date

        return self

    @model_validator(mode="after")
    def check_end_date(self) -> "BaseDateParams":
        """Enforce end_date <= today."""

        current_date = datetime.now()

        if self.end_date:
            end_dt = datetime.strptime(self.end_date, "%Y-%m-%d")

            if end_dt > current_date:
                print(
                    f"The end_date {self.end_date} is invalid. Set to today {current_date}."
                )
                self.end_date = current_date.strftime("%Y-%m-%d")

        return self


INTERVALS = Literal["1m", "15m", "30m", "1h", "1d"]
FINANCIAL_STATEMENTS = Literal["income", "balance", "cash"]
PERIODS = Literal["annual", "quarter"]


class BaseOtherParams(BaseModel):
    """Base class to validate other params (not start_date end_date) in function.

    Base validation rules:
    - symbol must be a string
    - limit must be an integer. Set to default as 100, if not provided
    - interval must be in Literal. Set to default as "1d"
    - financial_statement must be in Literal. Set to default as "income"
    - period must be in Literal. Set to default as "annual"
    """

    symbol: str
    limit: int = 100
    interval: INTERVALS = "1d"
    financial_statement: FINANCIAL_STATEMENTS = "income"
    period: PERIODS = "annual"

    @field_validator("symbol")
    @classmethod
    def upper_str(cls, v: str) -> str:
        """Convert a string to uppercase."""

        if isinstance(v, str):
            v = v.upper()
        return v
