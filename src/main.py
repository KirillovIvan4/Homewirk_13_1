from utils import utils
import class_category,class_product, class_smartphone

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
# Получение класса из строки
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
# Замена цены
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

print()

# for product in class_iterator_category.Iterator_category(list_category[0]):
#     print(product)

smart_iphone = class_smartphone.Smartphone("Iphone 15", "512GB, Gray space", 2100000.0, 25, "China", "15", "512 GB", "Gray space")
# print(type(smart_iphone))
# print(type(list_category[0].product[0]))
# print(type(smart_iphone) == type(list_category[0].product[0]))
# print(smart_iphone)


sum_price1 = list_category[0].product[0] + list_category[0].product[1]
print(f"Сумма цен продуктов {sum_price1}")
# sum_price2 = list_category[0].product[0] + smart_iphone
# print(f"Сумма цен продуктов {sum_price2}")
print(repr(smart_iphone))