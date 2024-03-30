from class_product import Product

class Smartphone(Product):
    def __init__(self,name ,description ,price ,quantity, performance, model, memory_capacity, color):
        super().__init__(name ,description ,price ,quantity)
        self.performance = performance
        self.model =model
        self.memory_capacity =memory_capacity
        self.color = color