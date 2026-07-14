from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import get_settings

settings = get_settings()

client: AsyncIOMotorClient | None = None


async def connect_to_mongo() -> None:
    global client
    client = AsyncIOMotorClient(settings.mongodb_uri, tz_aware=True)


async def close_mongo_connection() -> None:
    global client
    if client is not None:
        client.close()
        client = None


def get_db() -> AsyncIOMotorDatabase:
    if client is None:
        raise RuntimeError("MongoDB client is not initialized")

    return client[settings.mongodb_db]
