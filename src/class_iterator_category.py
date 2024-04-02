class IteratorCategory:
    def __init__(self, category):
        self.category = category
        self.stop = len(category.product)

    def __repr__(self):
        return f"{self.category} {self.stop}"

    def __iter__(self):
        self.value = -1
        return self
    def __next__(self):
        if self.value + 1 < self.stop:
            self.value += 1
            # return self.value
            return self.category.product[self.value]
        else:
            raise StopIteration
