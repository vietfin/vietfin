"""The VietFin Object."""

from pydantic import BaseModel
from typing import Generic, TypeVar, Literal, Any
import pandas as pd
from numpy import ndarray

from vietfin.utils.errors import VietFinError
from vietfin.utils.helpers import basemodel_to_df
from vietfin.standard_models.data import Data

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

    """

    results: T | None
    provider: str | None

    def __repr__(self) -> str:
        """Human readable representation of the VietFin object."""
        items = [
            f"{k}: {v}"[:83] + ("..." if len(f"{k}: {v}") > 83 else "")
            for k, v in self.model_dump().items()
        ]
        return f"{self.__class__.__name__}\n\n" + "\n".join(items)

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
        """Convert results field of the VfObject class to a dictionary using any of pandas to_dict options.

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
            del results["index"]
        return results
