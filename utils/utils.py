import json


def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('../products.json', 'r', encoding='utf-8') as json_data_products:
        data_products = json.load(json_data_products)
        return data_products



