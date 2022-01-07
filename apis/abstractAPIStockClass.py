from abc import ABC, abstractmethod


class AbstractAPIStockClass(ABC):
    @abstractmethod
    def stock_price(self):
        pass
