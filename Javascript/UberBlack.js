class UberBlack extends Car {
    constructor(license, driver, brand, typeCar_Accepted, seats) {
        super(license, driver);
        this.brand = brand;
        this.typeCar_Accepted = typeCar_Accepted;
        this.seats = seats;
    }
    printDataCar() {
        super.printDataCar();
        console.log(this.brand);
    }
}