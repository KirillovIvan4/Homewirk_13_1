from utils import utils
import class_Category,class_Product

data_category = utils.get_list()
list_category = []

for i in range (len(data_category)):
    list_products = []
    for j in range (len(data_category[i]['products'])):
        #print(data_category[i]['products'][j])
        path_product = data_category[i]['products'][j]
        product = class_Product.Product(path_product['name'], path_product['description'], path_product['price'], path_product['quantity'])
        list_products.append(product)

    category = class_Category.Category(data_category[i]['name'], data_category[i]['description'], data_category[i]['products'])
    list_category.append(category)
print(list_category)