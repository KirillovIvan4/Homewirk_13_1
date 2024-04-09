from class_abstract_category import AbstractCategory


class Order(AbstractCategory):

    def __init__(self,product, quantity:int):
        self.quantity = quantity
        self.product = product
        # self.price = product.price * quantity

    def __repr__(self):
        return f"{self.__class__}, {self.obgect_product}, {self.quantity}"
    def __str__(self):
        return f"В корзину добавлен заказ {self.obgect_product.name} в количестве:{self.quantity} стоимостью :self.price"

    # @classmethod
    # def add_order(cls, name_product,quantity_product, list_category):
    #     name_product = name_product
    #     quantity_product =  quantity_product
    #     for category in list_category:
    #         for product in category.product:
    #             print(product.name)
    #             if name_product == product.name:
    #                 print("Продукт найден")
    #                 if quantity_product <= product.quantity:
    #                     print("Количества хватает")
    #                     return cls(product, quantity_product, product.price)
    #                 # else:
    #                 #     return "Не достаточное количество продукта"
    #             # else:
    #             #     return "Такого продукта нет"
    # def add_product(self):
    #     pass

