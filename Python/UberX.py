from car import Car


class UberX(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model

    def print_data(self):
        super().print_data()
        print('Uber Car Info')
        print('Brand: ' + self.brand)
        print('Model: ' + self.model)
        print('-' * 20)
