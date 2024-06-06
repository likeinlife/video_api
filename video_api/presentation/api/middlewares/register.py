from fastapi import FastAPI

from . import logger


def register(app: FastAPI) -> None:
    logger.register(app)
