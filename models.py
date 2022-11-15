from beanie import Indexed, Document, Insert, Replace, before_event, ValidateOnSave
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
from enum import Enum
from pymongo import TEXT


class Rep(str, Enum):
    REP1 = "Rep1"
    REP2 = "Rep2"
    REP3 = "Rep3"
    REP4 = "Rep4"
    REP5 = "Rep5"
    REP6 = "Rep6"
    REP7 = "Rep7"
    REP8 = "Rep8"
    REP9 = "Rep9"
    REP10 = "Rep10"
    REP11 = "Rep11"
    REP12 = "Rep12"
    REP13 = "Rep13"
    REP14 = "Rep14"
    REP15 = "Rep15"
    REP16 = "Rep16"
    REP17 = "Rep17"
    REP18 = "Rep18"
    REP19 = "Rep19"
    REP20 = "Rep20"
    REP21 = "Rep21"
    REP22 = "Rep22"
    REP23 = "Rep23"
    REP24 = "Rep24"
    REP25 = "Rep25"
    REP26 = "Rep26"
    REP27 = "Rep27"
    REP28 = "Rep28"
    REP29 = "Rep29"
    REP40 = "Rep40"
    REP41 = "Rep41"


class Distributor(str, Enum):
    CARDINAL = "Cardinal"
    HENRYSCHEIN = "HenrySchein"
    OWENSMINOR = "OwensMinor"
    MEDLINE = "Medline"
    NDC = "NDC"
    CONCORDANCE = "Concordance"
    MCKESSON = "McKesson"
    BUSSE = "Busse"


class MONTH(str, Enum):
    JAN = "Jan"
    FEB = "Feb"
    MAR = "Mar"
    APR = "Apr"
    MAY = "May"
    JUN = "Jun"
    JUL = "Jul"
    AUG = "Aug"
    SEP = "Sep"
    OCT = "Oct"
    NOV = "Nov"
    DEC = "Dec"


class EndUser(BaseModel):
    name: str
    address: str
    address2: Optional[str] = None
    city: str
    state: str
    zip: str
    country: Optional[str] = None


YEAR = datetime.now().year + 1
MONTHS = [m.value for m in MONTH]
DISTRIBUTORS = [d.value for d in Distributor]


def valid_key(key: str):
    month, year, distributor = key.split("_")

    if month not in MONTHS:
        raise ValueError("Month must be one of: " + ", ".join(MONTHS))
    if len(year) != 4:
        raise ValueError("Year must be 4 digits")
    if int(year) < 2015 or int(year) > YEAR:
        raise ValueError(f"Year must be between 2015 and {YEAR}")
    if distributor not in DISTRIBUTORS:
        raise ValueError("Distributor must be one of: " + ", ".join(DISTRIBUTORS))

    return True


class Tracing(Document):
    rep: Rep
    item: Indexed(str, index_type=TEXT)
    commission: float
    date_of_sale: datetime
    key: Indexed(str)  # MONTH_YEAR_DISTRIBUTOR
    enduser: EndUser
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @before_event([Insert, Replace])
    def updated_at_event(self):
        self.updated_at = datetime.now()

    @before_event(Insert)
    def created_at_event(self):
        self.created_at = datetime.now()

    class Settings:
        name = "tracings"
        use_cache = True
        cache_expiration_time = timedelta(seconds=30)
        cache_capacity = 5
        validate_on_save = True

    class Config:
        schema_extra = {
            "example": {
                "rep": "Rep1",
                "item": "723",
                "commission": 0.04,
                "date_of_sale": datetime(2021, 1, 1, 0, 0, 0),
                "key": "Jan_2021_Cardinal",
                "enduser": {
                    "name": "John Doe",
                    "address": "123 Main St",
                    "address2": "Apt 1",
                    "city": "New York",
                    "state": "NY",
                    "zip": "10001",
                    "country": "USA",
                },
            }
        }


# class TracingUpdate(Document):
#     """Updatable tracing fields"""

#     rep: Optional[Rep] = None
#     item: Optional[str] = None
#     end_user: Optional[EndUser] = None
#     commission: Optional[float] = None
#     date_of_sale: Optional[datetime] = None

#     @property
#     def date_of_entry(self):
#         return self._id.generation_time
