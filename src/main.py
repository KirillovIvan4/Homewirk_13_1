from utils import utils
import class_Category,class_Product

data_category = utils.get_list()
list_category = []

for i in range (len(data_category)):
    list_products = []
    for j in range (len(data_category[i]['products'])):
        path_product = data_category[i]['products'][j]
        product = class_Product.Product(path_product['name'], path_product['description'], path_product['price'], path_product['quantity'])
        list_products.append(product)

    category = class_Category.Category(data_category[i]['name'], data_category[i]['description'], list_products)
    list_category.append(category)
print(list_category)
print()
test_1 = class_Product.Product("test_smart", 'description', 100, 1)
list_category[0].add_product = test_1
print(list_category)
print()
for item in range(len(list_category)):
    print(list_category[item].name)
    print(list_category[item].get_product_and_price_and_quantity)