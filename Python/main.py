from car import Car

if __name__ == '__main__':
    car = Car()
    car.license = 'ABC-123'
    car.driver = 'John'
    print('La licencia es :' + car.license)
    print('El conductor es :' + car.driver)
