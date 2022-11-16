from motor.motor_asyncio import AsyncIOMotorClient
from config import CONFIG
from beanie import init_beanie

from models import Tracing

from pymongo import MongoClient


async def Init():
    db = AsyncIOMotorClient(CONFIG.mongodb_uri).busse
    await init_beanie(
        db,
        document_models=[
            Tracing,
        ],
    )


def clear_indexes(coll: str):
    db = MongoClient(CONFIG.mongodb_uri).busse
    coll = db.get_collection(coll)
    if coll is not None:
        # drop indexes
        res = coll.drop_indexes()

        return res
