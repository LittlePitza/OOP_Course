from car import Car


class UberVan(Car):
    typeCar_Accepted = []
    seats_Material = []

    def __init__(self, license, driver, typeCar_Accepted, seats_Material):
        super().__init__(license, driver)
        self.typeCar_Accepted = typeCar_Accepted
        self.seats_Material = seats_Material

    def print_data(self):
        super().print_data()
        print('Type Car Accepted: ' + str(self.typeCar_Accepted))
        print('Seats Material: ' + str(self.seats_Material))
        print('-' * 20)
