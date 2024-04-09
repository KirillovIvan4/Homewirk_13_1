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
        return f"{self.name} \n{self.__products} "


    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.__len__(self)} шт."

    def __len__(self):
        sum_products = 0
        for products in self.__products:
            sum_products += products.quantity
        return sum_products


    @property
    def product(self):
        """Геттер возвращает список с объектами Product"""
        return self.__products

    @product.setter
    def product(self, object_products):
        """ Сеттер получает на вход новый объект Product, сравнивает с уже имеющемися.
        Если объект с таким же параметром name уже есть то их кол-во складывается, а цена сравнивается для выбора более высокой"""
        # Счетчик количества пройденых циклов в которых Product.name не совпадают
        # если счетчик равен длинне списка то можно добавлять новый объект так как он ни разу не встретился
        occurrences = 0
        for product in self.__products:
            if isinstance(object_products,type(product)) and issubclass(type(object_products),type(product)) and object_products.name != product.name:
            # if object_products.name != product.name:
                occurrences += 1

        if occurrences == len(self.__products):
            self.__products.append(object_products)
        # если счетчик не равен длинне списка это значит что объект с таким же name уже есть и нужно сложить их количество и выбрать более высокую цену
        else:
            for product in self.__products:
                if object_products.name == product.name:
                    product.quantity += object_products.quantity
                    if product.price < object_products.price:
                        product.price = object_products.price



    @property
    def product_and_price_and_quantity(self):
        """Геттер возращает строку с информацией о продукте в виде:Продукт, 80 руб. Остаток: 15 шт."""
        list_products = []
        for product in self.__products:
            list_products.append(f"{product}")
        return list_products
    def get_average_price(self):
        """Метод возвращает среднею цену рподукта в категории, если количество продукта равно 0, то возвращает 0"""
        summ_price = 0
        quantity_product = 0
        try:
            for products in self.__products:
                price = products.price
                summ_price += price
                quantity_product += 1

            average_price = summ_price / quantity_product
        except ZeroDivisionError:
            return 0
        else:
            return average_price



