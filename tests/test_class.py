import pytest
from io import StringIO

from src import class_category,class_product

@pytest.fixture()
def class_products_1():
    return class_product.Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture()
def class_products_2():
    return class_product.Product("Iphone 15", "512GB, Gray space", 210000.0, 25)

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


def test_init_products(class_products_1):
    assert class_products_1.name == "Samsung Galaxy C23 Ultra"
    assert class_products_1.description == "256GB, Серый цвет, 200MP камера"
    assert class_products_1.price == 180000.0
    assert class_products_1.quantity == 5


# def test_add_product(class_smart):
#     class_smart.product = class_products_1
#     assert class_smart.product() == ["Samsung Galaxy C23 Ultra", "Iphone 15"]

def test_get_product_and_price_and_quantity(class_smart):
    assert class_smart.product_and_price_and_quantity == ["Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт"]


def test_from_string(class_smart):
    test_new_product = class_product.Product.from_string("test_smart description 100 1")
    assert test_new_product.name == "test_smart"
    assert test_new_product.description == "description"
    assert test_new_product.price == 100.0
    assert test_new_product.quantity == 1

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