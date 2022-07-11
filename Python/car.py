from account import Account


class Car:

    id = int
    license = str
    driver = Account("John", "123456789")
    passenger = 0

    def __init__(self, license, driver):
        self.id = ""
        self.license = license
        self.driver = driver
        self.passenger = 0

    def print_data(self):
        print('-' * 40)
        if self.id == "":
            print("Car ID: Not registered")
        else:
            print("Car ID: {}".format(self.id))
        print('License: ' + self.license)
        print('Driver: ' + self.driver.name)
        print('Passenger: ' + str(self.passenger))
        print('-' * 20)
