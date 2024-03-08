"""Fmarket Mutual Fund Historical NAV per Share Performance Model."""

from vietfin.abstract.data import Data
from vietfin.utils.helpers import ValidatedDatetime


class FmarketFundHistoricalNavPerformanceData(Data):
    """Fmarket Mutual Fund Historical NAV per Share Performance Data."""

    __alias_dict__ = {
        "percent_change_to_previous": "navToPrevious",
        "percent_change_to_last_year": "navToLastYear",
        "percent_change_to_beginning": "navToBeginning",
        "percent_change_1m": "navTo1Months",
        "percent_change_3m": "navTo3Months",
        "percent_change_6m": "navTo6Months",
        "percent_change_12m": "navTo12Months",
        "percent_change_24m": "navTo24Months",
        "percent_change_36m": "navTo36Months",
        "percent_change_36m_annualized": "annualizedReturn36Months",
        "update_at": "updateAt",
    }

    percent_change_to_previous: float | None
    percent_change_to_last_year: float | None
    percent_change_to_beginning: float | None
    percent_change_1m: float | None
    percent_change_3m: float | None
    percent_change_6m: float | None
    percent_change_12m: float | None
    percent_change_24m: float | None
    percent_change_36m: float | None
    percent_change_36m_annualized: float | None
    update_at: ValidatedDatetime | None
