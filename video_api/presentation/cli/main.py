import asyncio
import json
import sys
from pathlib import Path

sys.path.append("/opt/app")

from container import get_container
from domain.entities.advert import Advert
from domain.values.positive_int import PositiveInt
from logic.interactors.advert import AdvertInteractor


def get_adverts() -> list[Advert]:
    adverts: list[Advert] = []
    with Path("/opt/static/adverts.json").open("r", encoding="UTF-8") as f:
        j = json.load(f)
        for obj in j:
            adverts.append(  # noqa: PERF401
                Advert(
                    title=obj["title"],
                    author=obj["author"],
                    view_count=PositiveInt(obj["view_count"]),
                    position=PositiveInt(obj["position"]),
                ),
            )
    return adverts


async def fill_db() -> None:
    container = get_container()
    interactor = container.get(AdvertInteractor)
    adverts = get_adverts()
    [await interactor.create(i) for i in adverts]
    print(f"Filled DB with adverts. Count - {len(adverts)}")  # noqa: T201


if __name__ == "__main__":
    asyncio.run(fill_db())
