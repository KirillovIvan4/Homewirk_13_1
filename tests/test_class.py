import pytest

from src import class_

@pytest.fixture()
def class_products():
    return class_.Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def class_smart(class_products):
    return class_.Category("Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    [class_products])


def test_init_category(class_smart):
  assert class_smart.name == "Смартфоны"
  assert class_smart.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
  assert class_smart.products[0].name == 'Samsung Galaxy C23 Ultra'


def test_nummer_of_category(class_smart):
    assert  class_smart.nummer_of_category == 3


def test_nummer_of_products(class_smart):
    assert  class_smart.nummer_of_products == 1


def test_init_products(class_products):
    assert class_products.name == "Samsung Galaxy C23 Ultra"
    assert class_products.description == "256GB, Серый цвет, 200MP камера"
    assert class_products.price == 180000.0
    assert class_products.quantity == 5