"""SSI Index Search Model."""

from vietfin.abstract.data import Data


class SsiIndexSearchData(Data):
    """SSI Index Search Data."""

    __alias_dict__ = {
        "index_symbol": "comGroupCode",
        "group_by_index": "parentComGroupCode",
    }

    index_symbol: str  # Symbol of an index.
    group_by_index: str  # The parent index from which the given index is derived.