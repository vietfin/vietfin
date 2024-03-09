"""TCBS Equity Profile Model."""

from pydantic import AnyHttpUrl, field_validator
from bs4 import BeautifulSoup as bs

from vietfin.abstract.data import Data


class TcbsEquityProfileData(Data):
    """TCBS Equity Profile Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "name": "shortName",
        "legal_name": "companyName",
        "exchange": "exchange",
        "long_description": "companyProfile",
        "company_url": "website",
        "employees": "noEmployees",
        "industry_category": "industry",
    }

    symbol: str  # Symbol representing the entity requested in the data.
    name: str  # Common name of the company.
    legal_name: str  # Official legal name of the company.
    exchange: str | None = None  # Stock exchange where the stock ticker is traded.
    long_description: str | None = None  # Long description of the company.
    company_url: AnyHttpUrl | None = None  # URL of the company's website.
    employees: int | None = None  # Number of employees working for the company.
    industry: str | None = None  # Category of industry in which the company operates.
    
    @field_validator("long_description")
    @classmethod
    def parse_html(cls, v: str) -> str:
        """Parse HTML to text."""
        soup = bs(v, "html.parser")
        v = soup.get_text(separator="\n", strip=True)
        return v