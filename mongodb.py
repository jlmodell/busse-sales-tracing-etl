from motor.motor_asyncio import AsyncIOMotorClient
from config import CONFIG
from beanie import init_beanie

from models import Tracing


async def Init():
    db = AsyncIOMotorClient(CONFIG.mongodb_uri).busse
    await init_beanie(
        db,
        document_models=[
            Tracing,
        ],
    )
