class Car:

    def __init__(self, id, license, driver):
        self.id = id
        self.license = license
        self.driver = driver
        self.passenger = 0

    def print_data(self):
        print('Car ID: ' + str(self.id))
        print('License: ' + self.license)
        print('Driver: ' + self.driver)
        print('Passenger: ' + str(self.passenger))
        print('-' * 20)
