class UberVan extends Car{
    constructor(license, driver, typeCar_Accepted , seats) {
        super(license, driver);
        this.seats = seats;
        this.typeCar_Accepted = typeCar_Accepted;
    }
    printDataCar() {
        super.printDataCar();
        console.log(this.seats);
    }
}