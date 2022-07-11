from car import Car
from account import Account

if __name__ == '__main__':

    print('Hello World!')

    car = Car('Pitza-123', Account('John', '123456789'))
    print(vars(car))
    print(vars(car.driver))
    car.print_data()

    car.id = 'ABC-1234'
    car.passenger = 3
    car.print_data()

