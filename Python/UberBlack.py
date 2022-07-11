from car import Car


class UberBlack(Car):
    typeCar_Accepted = []
    seats_Material = []

    def __int__(self, license, driver, typeCar_Accepted, seats_Material):
        super().__init__(license, driver)
        self.typeCar_Accepted = typeCar_Accepted
        self.seats_Material = seats_Material

