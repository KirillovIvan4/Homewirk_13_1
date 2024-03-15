from utils import utils


class Category:
    name = str
    description = str
    products = list
    nummer_of_category = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.nummer_of_category += 1
        self.nummer_of_products = len(self.products)


class Product:
    name = str
    description = str
    price = float
    quantity = int
    def __init__(self,name ,description ,price ,quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity =quantity


data_category = utils.get_list()
list_category = []
for i in data_category:
    category = Category(i['name'], i['description'], i['products'])
    list_category.append(category)
print(list_category)
print(Category.nummer_of_category)
print(list_category[1].nummer_of_products)