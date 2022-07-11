from car import Car
from account import Account
from UberX import UberX
from UberVan import UberVan

if __name__ == '__main__':

    print('Hello World!')

    car = Car('Pitza-123', Account('John', '123456789'))
    print(vars(car))
    print(vars(car.driver))
    car.print_data()

    car.id = 'ABC-1234'
    car.passenger = 3
    car.print_data()

    # Create an instance of UberX
    uberX = UberX('Pitza-123', Account('John', '123456789'), 'BMW', '2017')
    uberX.print_data()

    # Create an instance of UberVan
    uberVan = UberVan('Pitza-123', Account('John', '123456789'), ['A', 'B'], ['Leather', 'Plastic'])
    uberVan.print_data()


