from utils import utils
import class_category,class_product

data_category = utils.get_list()
list_category = []

for i in range (len(data_category)):
    list_products = []
    for j in range (len(data_category[i]['products'])):
        path_product = data_category[i]['products'][j]
        product = class_product.Product(path_product['name'], path_product['description'], path_product['price'], path_product['quantity'])
        list_products.append(product)

    category = class_category.Category(data_category[i]['name'], data_category[i]['description'], list_products)
    list_category.append(category)
print(list_category)
print()

test_1 = class_product.Product.from_string("test_smart description 100 1")
test_2 = class_product.Product.from_string("test_smart description 200 1")
test_3 = class_product.Product.from_string("test_smart description 10 1")
list_category[0].product = test_1
print(list_category)
list_category[0].product = test_2
print(list_category)
list_category[0].product = test_3
print(list_category)
print()

for category_ in range(len(list_category)):
    print(list_category[category_].name)
    for product_ in range(len(list_category[category_].product_and_price_and_quantity)):
        print(list_category[category_].product_and_price_and_quantity[product_])
print()

# print(f"{list_category[0].product[0].name}: {list_category[0].product[0].price}")
print(list_category[0].product_and_price_and_quantity[0])
list_category[0].product[0].new_price = 0.0
print(list_category[0].product_and_price_and_quantity[0])
list_category[0].product[0].new_price = -1.0
print(list_category[0].product_and_price_and_quantity[0])

list_category[0].product[0].new_price = 10
print(list_category[0].product_and_price_and_quantity[0])
list_category[0].product[0].new_price = 580000.0
print(list_category[0].product_and_price_and_quantity[0])
print()

for category_ in list_category:
    print(category_)

print()

print(list_category[0].product[0])
print(list_category[0].product[1])
sum_price = list_category[0].product[0] + list_category[0].product[1]
print(f"Сумма цен продуктов {sum_price}")