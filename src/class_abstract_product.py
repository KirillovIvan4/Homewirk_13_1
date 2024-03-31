from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    pass

    @abstractmethod
    def __add__(self,other):
        pass


    @abstractmethod
    def from_string(self):
         pass

    @abstractmethod
    def new_price(self):
        pass