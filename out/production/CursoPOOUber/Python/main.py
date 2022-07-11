from car import Car

if __name__ == '__main__':
    car = Car('ABC-123', 'ABC-123', 'John')
    car.passenger = 4
    car.print_data()

    car2 = Car('ABC-456', 'ABC-456', 'Mary')
    car2.passenger = 8
    car2.print_data()

    car3 = Car('ABC-789', 'ABC-789', 'Bob')
    car3.passenger = 2
    car3.print_data()

