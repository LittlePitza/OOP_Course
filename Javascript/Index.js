let car = new Car("ABC-123", new Account("Juan", "Perez"));
car.passenger = 4;
car.printDataCar();

let uberX = new UberX("UberX-456", new Account("Juan", "Perez"),
    "Chevrolet", "Spark");
uberX.passenger = 4;
uberX.printDataCar();