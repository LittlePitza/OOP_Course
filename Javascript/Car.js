// function Car(license, driver) {
//     this.id = 0;
//     this.license = license;
//     this.driver = driver;
//     this.passenger = 0;
// }
//
// Car.prototype.printDataCar = function () {
//     console.log(this.driver);
//     console.log(this.driver.name)
//     console.log(this.license);
//     console.log(this.passenger);
// } // old way to create a class

class Car {
    constructor(license, driver) {
        this.id = undefined;
        this.license = license;
        this.driver = driver;
        this.passenger = 0;
    }
    printDataCar() {
        console.log(this.driver);
        console.log(this.driver.name)
        console.log(this.license);
        console.log(this.passenger);
    }
}