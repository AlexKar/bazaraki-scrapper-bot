from typing import List

from api.bazaraki_api import BazarakiApi
from scrapper.ad import Ad, Category
from scrapper.scrapper import Scrapper

MIN_PRICE = 0
MAX_PRICE = 30000

class CarAdsManager:
    def __init__(self, api: BazarakiApi, scrapper: Scrapper):
        self._api = api
        self._scrapper = scrapper

    def get_cars_ads(self, page: int) -> List[Ad]:
        district = []
        min_price = MIN_PRICE
        max_price = MAX_PRICE
        cars_html = self._api.get_cars([district], min_price, max_price, page)
        return self._scrapper.scrap(cars_html, Category.CARS)
