import class_product

class LawnGrass(class_product.Product):
    def __init__(self,name ,description ,price ,quantity, manufacturer_country, germination_period, color):
        super().__init__(name ,description ,price ,quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color


