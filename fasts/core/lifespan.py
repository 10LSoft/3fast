from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise


def get_lifespan(config: dict):
    """
    Lifespan function for Tortoise ORM.
    """
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Initialize Tortoise ORM
        print("Initializing Tortoise ORM...")
        await Tortoise.init(config=config)
        await Tortoise.generate_schemas()

        yield

        # Close Tortoise ORM connections
        print("Closing Tortoise ORM connections...")
        await Tortoise.close_connections()

    return lifespan
