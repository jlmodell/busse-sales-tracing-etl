# import pandas as pd
import asyncio
from rich import print
from datetime import datetime

from mongodb import Init, clear_indexes
from models import Tracing, Rep, Distributor


async def main():
    # print(clear_indexes("tracings"))
    # init db
    await Init()

    # insert data
    await insert_tracing()

    # get all documents
    docs = await Tracing.find().to_list()
    print(docs)


async def insert_tracing():
    await Tracing(
        rep=Rep.REP15,
        item="6417R2",
        sale=1000,
        commission=0.08,
        date_of_sale=datetime(2022, 1, 1, 0, 0, 0),
        key="Jan_2022_Busse",
        name="name1",
        address="address1",
        address2="address2",
        city="city1",
        state="state1",
        zip="zip1",
        country="country1",
    ).save()


if __name__ == "__main__":
    asyncio.run(main())
