# import pandas as pd
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import asyncio
from rich import print
from datetime import datetime

from mongodb import Init
from models import Tracing, Rep, Distributor, EndUser
from config import CONFIG


async def main():
    # init db
    await Init()

    # insert data
    # await insert_tracing()

    # get all documents
    docs = await Tracing.find(Tracing.rep == Rep.REP15).to_list()
    print(docs)


async def insert_tracing():
    await Tracing(
        rep=Rep.REP1,
        item="6417R2",
        commission=1.0,
        date_of_sale=datetime(2022, 1, 1, 0, 0, 0),
        key="Jan_2022_Busse",
        enduser=EndUser(
            name="name1",
            address="address1",
            address2="address2",
            city="city1",
            state="state1",
            zip="zip1",
            country="country1",
        ),
    ).save()


if __name__ == "__main__":
    asyncio.run(main())
