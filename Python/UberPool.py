from car import Car


class UberPoll(Car):
    brand = str
    model = str
    capacity = int

    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model
        self.capacity = 0
