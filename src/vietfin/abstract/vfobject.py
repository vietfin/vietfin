"""The VietFin Object."""

from pydantic import BaseModel
from typing import Generic, TypeVar, Literal, Any, TYPE_CHECKING
import pandas as pd
from numpy import ndarray

from vietfin.utils.errors import VietFinError
from vietfin.utils.helpers import basemodel_to_df
from vietfin.abstract.data import Data

# Handles type hinting and conditionally imports DataFrame from polars library when to_polars() method is used.
if TYPE_CHECKING:
    try:
        from polars import DataFrame as PolarsDataFrame  # type: ignore
    except ImportError:
        PolarsDataFrame = None

T = TypeVar("T")


class VfObject(BaseModel, Generic[T]):
    """VietFin Object.

    source: https://github.com/OpenBB-finance/OpenBBTerminal/blob/develop/openbb_platform/core/openbb_core/app/model/obbject.py

    The VfObject (VietFin Object) is at the heart of developing around the VietFin project.
    Every command will return this class as the command output.
    This class contains the following attributes.

    Attributes
    ----------
    results :
        Serializable results
    provider : str
        Provider name
    extra :
        Additional metadata about the command run,
        generated by generate_extra_metadata() in ~/utils/helpers.py
    raw_data : dict | list[dict]
        Raw data returned by the API call.
        This is useful for users who want to parse the API response themselves.
    """

    results: T | None
    provider: str | None
    extra: dict[str, Any] | None
    raw_data: dict[Any, Any] | list[dict[Any, Any]] | None

    def __repr__(self) -> str:
        """Human readable representation of the VietFin object."""
        items = [
            f"{k}: {v}"[:83] + ("..." if len(f"{k}: {v}") > 83 else "")
            for k, v in self.model_dump().items()
        ]
        return f"{self.__class__.__name__}\n\n" + "\n".join(items)

    def __len__(self) -> int:
        """Return the number of elements in the results attribute of the VietFin object.

        Overloading the __len__() method to make the VietFin object behave like a list.

        """
        return self.to_df().shape[0]  # number of rows in the dataframe

    def to_df(
        self, index: str | None = None, sort_by: str | None = None
    ) -> pd.DataFrame:
        """Convert results field to pandas dataframe.

        Supports converting creating pandas DataFrames from the following
        serializable data formats:

        - List[BaseModel]
        - List[Dict]
        - List[List]
        - List[str]
        - List[int]
        - List[float]
        - Dict[str, Dict]
        - Dict[str, List]
        - Dict[str, BaseModel]

        Parameters
        ----------
        index : Optional[str]
            Column name to use as index.
        sort_by : Optional[str]
            Column name to sort by.

        Returns
        -------
        pd.DataFrame
            Pandas dataframe.

        """

        def is_list_of_basemodel(items: list[T] | T) -> bool:
            return isinstance(items, list) and all(
                isinstance(item, BaseModel) for item in items
            )

        if self.results is None or not self.results:
            raise VietFinError("Results not found.")

        if isinstance(self.results, pd.DataFrame):
            return self.results

        try:
            res = self.results
            df = pd.DataFrame()
            sort_columns = True

            # List[Dict]
            if (
                isinstance(res, list)
                and len(res) == 1
                and isinstance(res[0], dict)
            ):
                r = res[0]
                dict_of_df = {}

                for k, v in r.items():
                    # Dict[str, List[BaseModel]]
                    if is_list_of_basemodel(v):
                        dict_of_df[k] = basemodel_to_df(v, index or "date")
                        sort_columns = False
                    # Dict[str, Any]
                    else:
                        dict_of_df[k] = pd.DataFrame(v)

                df = pd.concat(dict_of_df, axis=1)

            # List[BaseModel]
            elif is_list_of_basemodel(res):
                dt: list[Data] | Data = res  # type: ignore
                df = basemodel_to_df(dt, index or "date")
                sort_columns = False
            # List[List | str | int | float] | Dict[str, Dict | List | BaseModel]
            else:
                try:
                    df = pd.DataFrame.from_records(res)
                    # Set index, if any
                    if index and index in df.columns:
                        df.set_index(index, inplace=True)

                except ValueError:
                    if isinstance(res, dict):
                        df = pd.DataFrame([res])

            if df is None:
                raise VietFinError("Unsupported data format.")

            # Drop columns that are all NaN, but don't rearrange columns
            if sort_columns:
                df.sort_index(axis=1, inplace=True)
            df = df.dropna(axis=1, how="all")

            # Sort by specified column
            if sort_by:
                df.sort_values(by=sort_by, inplace=True)

        except VietFinError as e:
            raise e
        except ValueError as ve:
            raise VietFinError(
                f"ValueError: {ve}. Ensure the data format matches the expected format."
            ) from ve
        except TypeError as te:
            raise VietFinError(
                f"TypeError: {te}. Check the data types in your results."
            ) from te
        except Exception as ex:
            raise VietFinError(f"An unexpected error occurred: {ex}") from ex

        return df

    def to_numpy(self) -> ndarray:
        """Convert results field to numpy array."""
        return self.to_df().reset_index().to_numpy()

    def to_dict(
        self,
        orient: Literal[
            "dict", "list", "series", "split", "tight", "records", "index"
        ] = "list",
    ) -> dict[str, list]:
        """Convert results field of the VfObject class to a dictionary of lists using any of pandas to_dict options.

        Parameters
        ----------
        orient : Literal["dict", "list", "series", "split", "tight", "records", "index"]
            Value to pass to `.to_dict()` method


        Returns
        -------
        Dict[str, List]
            Dictionary of lists.

        """
        df = self.to_df()  # type: ignore
        transpose = False
        if orient == "list":
            transpose = True
            if not isinstance(self.results, dict):
                transpose = False
            else:  # Only enter the loop if self.results is a dictionary
                self.results: dict[str, Any] = self.results  # type: ignore
                for _, value in self.results.items():
                    if not isinstance(value, dict):
                        transpose = False
                        break
        if transpose:
            df = df.T
        results = df.to_dict(orient=orient)
        if orient == "list" and "index" in results:
            del results["index"]  # type: ignore
        return results  # type: ignore

    def to_polars(self) -> "PolarsDataFrame":
        """Convert results field of the VfObject class to polars dataframe."""
        try:
            from polars import from_pandas  # type: ignore # pylint: disable=import-outside-toplevel
        except ImportError as exc:
            raise ImportError(
                "Please install polars: `pip install polars pyarrow`  to use this method."
            ) from exc

        return from_pandas(self.to_df(index=None))

    def to_csv(self, file_path: str) -> None:
        """Write results field of the VfObject class to a csv file.

        Parameters
        ----------
        file_path : str
            Path to the csv file.
            Ensure the file extension is .csv.
            If the file does not exist, it will be created.
            If the file exists, it will be overwritten.
        """
        df = self.to_df()
        try:
            df.to_csv(file_path, index=True)
        except Exception as ex:
            raise VietFinError(f"An unexpected error occurred: {ex}") from ex