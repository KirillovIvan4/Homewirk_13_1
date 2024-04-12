import pytest


from src import class_category, class_product

@pytest.fixture()
def class_products_1():
    return class_product.Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture()
def class_products_2():
    return class_product.Product("Iphone 15", "512GB, Gray space", 210000.0, 25)


@pytest.fixture()
def class_products_3():
    return class_product.Product("Iphone 15", "512GB, Gray space", 2100000.0, 25)

@pytest.fixture()
def class_smart(class_products_1):
    return class_category.Category("Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    [class_products_1])

def test_init_category(class_smart):
  assert class_smart.name == "Смартфоны"
  assert class_smart.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
  assert class_smart.product[0].name == "Samsung Galaxy C23 Ultra"



def test_nummer_of_category(class_smart):
    assert  class_smart.nummer_of_category == 2


def test_nummer_of_products(class_smart):
    assert  class_smart.nummer_of_products == 3

def test_len(class_smart):
    assert len(class_smart) == 5


def test_product_and_price_and_quantity(class_smart):
    assert class_smart.product_and_price_and_quantity == ["Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт"]


def test_from_string(class_smart):
    test_new_product = class_product.Product.from_string("test_smart description 100 1")
    assert test_new_product.name == "test_smart"
    assert test_new_product.description == "description"
    assert test_new_product.price == 100.0
    assert test_new_product.quantity == 1


def test_init_products(class_products_1, class_products_2):
    assert class_products_1.name == "Samsung Galaxy C23 Ultra"
    assert class_products_1.description == "256GB, Серый цвет, 200MP камера"
    assert class_products_1.price == 180000.0
    assert class_products_1.quantity == 5
    assert class_products_2.name == "Iphone 15"
    assert class_products_2.description == "512GB, Gray space"
    assert class_products_2.price == 210000.0
    assert class_products_2.quantity == 25

def test_add_product(class_products_3, class_products_2, class_products_1, class_smart):
    class_smart.product = class_products_2
    assert class_smart.product[1].quantity == 25
    class_smart.product = class_products_2
    assert class_smart.product[1].quantity == 50
    assert class_smart.product[1].price == 210000.0
    class_smart.product = class_products_3
    assert class_smart.product[1].price == 2100000.0


def test_new_price(class_products_1):
    class_products_1.new_price = 580000
    assert class_products_1.new_price == 580000
    class_products_1.new_price = -10
    assert class_products_1.new_price == 580000
    class_products_1.new_price = 0
    assert class_products_1.new_price == 580000
    # Ни как не разобраться как протестировать input
    # class_products_1.get_new_price = 10
    # assert class_products_1.get_new_price == 180000

def test_add(class_products_1, class_products_2):
    sum_price = (class_products_1.price * class_products_1.quantity) + (class_products_2.price * class_products_2.quantity)
    assert sum_price == 6150000.0

# def test_iterator_category (class_smart):
#     st = []
#     for i in class_iterator_category.Iterator_category(class_smart):
#         st.append(str(i))
#
#     assert st == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт']

def test_str(class_products_1):
    assert str(class_products_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт"
