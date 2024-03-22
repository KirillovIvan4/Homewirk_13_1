class Product:
    name : str
    description : str
    price : float
    quantity : int

    def __init__(self,name ,description ,price ,quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.correct_price = True

    def __repr__(self):
        return f"{self.name} {self.price}"

    @classmethod
    def from_string(cls,new_product):
        name, description, price, quantity = new_product.split(' ')
        price = float(price)
        quantity = int(quantity)
        return cls(name, description, price, quantity)
    @property
    def new_price(self):
        """Геттер возвращает цену или предупреждение о некоректно введеной цене"""
        return self.price


    @new_price.setter
    def new_price(self, new_price: float):
        """Сеттер принемает новую цену проверяет больше ли она 0 если меньше то меняет correct_price на False для вывода сообщения об ошибке
        если больше то сравнивает новую и старую цену для выбора большей"""
        self.correct_price = True
        if new_price > 0:
            if self.price < new_price:
                self.price = new_price
            else:
                print("Новая цена ниже уже установленной\nВведите 'y' для подтверждения новой цены")
                user_response = input()
                if user_response.lower() == "y":
                    self.price = new_price

        else:
            print("Цена введена некорректная")

