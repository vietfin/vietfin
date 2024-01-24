from .search import search
from .historical import historical
from vietfin.standard_models.vfobject import VfObject


class Fmarket:
    def __init__(self):
        pass

    @staticmethod
    def search(symbol: str, fund_type: str) -> VfObject:
        return search(symbol, fund_type)

    @staticmethod
    def historical(symbol: str) -> VfObject:
        return historical(symbol)
