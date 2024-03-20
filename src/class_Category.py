from utils import utils


class Category:
    name : str
    description : str
    __products : list
    nummer_of_category = 0
    nummer_of_products = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.nummer_of_category += 1
        Category.nummer_of_products += len(self.__products)


    def __repr__(self):
        return f"{self.name} \n{self.__products}"


    @property
    def add_product(self):
        return self.__products

    @add_product.setter
    def add_product(self, object_products):
        self.__products.append(object_products)

    @property
    def get_product_and_price_and_quantity(self):
        list_products = ""
        for product in self.__products:
            list_products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт \n"
        return list_products

# class Product:
#     name : str
#     description : str
#     price : float
#     quantity : int
#     def __init__(self,name ,description ,price ,quantity):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity =quantity
#
#     def __repr__(self):
#         return self.name


# data_category = utils.get_list()
# list_category = []
#
# for i in range (len(data_category)):
#     list_products = []
#     for j in range (len(data_category[i]['products'])):
#         #print(data_category[i]['products'][j])
#         path_product = data_category[i]['products'][j]
#         product = Product(path_product['name'], path_product['description'], path_product['price'], path_product['quantity'])
#         list_products.append(product)
#
#     category = Category(data_category[i]['name'], data_category[i]['description'], data_category[i]['products'])
#     list_category.append(category)
# print(list_category)
#
