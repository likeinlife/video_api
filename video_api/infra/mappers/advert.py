from domain.entities.advert import Advert
from domain.values.positive_int import PositiveInt
from infra.db.orm import AdvertORM


class AdvertORMMapper:
    @staticmethod
    def to_orm(advert: Advert) -> AdvertORM:
        return AdvertORM(
            title=advert.title,
            ad_id=advert.ad_id,
            author=advert.author,
            view_count=advert.view_count.as_generic_type(),
            position=advert.position.as_generic_type(),
        )

    @staticmethod
    def from_orm(advert: AdvertORM) -> Advert:
        return Advert(
            id=advert.id,
            ad_id=advert.ad_id,
            title=advert.title,
            author=advert.author,
            view_count=PositiveInt(advert.view_count),
            position=PositiveInt(advert.position),
        )
