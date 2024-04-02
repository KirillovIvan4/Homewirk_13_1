from class_abstract_category import AbstractCategory

class Order(AbstractCategory):

    @classmethod
    def add_order(cls, name_product, quantity_product, list_category):
        name_product = name_product
        quantity_product = quantity_product
        list_category = list_category





    def __init__(self,name:str,obgect_product , quantity:int):
        self.name = name
        self.quantity = quantity
        self.obgect_product = obgect_product
        self.price = 1

    def __repr__(self):
        return f"{self.__class__}, {self.name}, {self.quantity}"
    def __str__(self):
        return f"В корзину добавлен заказ {self.name} в количестве:{self.quantity} стоимостью :{self.quantity * self.price}"

    def product(self):

