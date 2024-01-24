"""VietFin helper functions."""

from typing import Iterable
from typing_extensions import Annotated
import re
import ast
from datetime import datetime, timezone

import pandas as pd
from pydantic.functional_validators import AfterValidator


from vietfin.standard_models.data import Data


def to_snake_case(string: str) -> str:
    """Convert a string to snake case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    return (
        re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        .lower()
        .replace(" ", "_")
        .replace("__", "_")
    )


def validate_datetime(v: datetime) -> datetime:
    """Validate datetime value.

    Return None if date before 1970-01-01.

    """
    # Compare to offset-aware datetime
    if v < datetime(1970, 1, 1, 0, 0).replace(tzinfo=timezone.utc):
        return None  # type: ignore
    return v


# Custom type created via Pydantic Annotated validator for datetime data type
ValidatedDatetime = Annotated[datetime, AfterValidator(validate_datetime)]


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
        df = df.set_index(index)
        # TODO: This should probably check if the index can be converted to a datetime instead of just assuming
        if df.index.name == "date":
            df.index = pd.to_datetime(df.index)
            df.sort_index(axis=0, inplace=True)

    return df
