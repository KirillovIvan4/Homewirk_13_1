class MixiAttribute:
    def __repr__(self):
        return f"Создан объект: {self.__class__} - {self.name}, {self.description}, {self.price}, {self.quantity}"