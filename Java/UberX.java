package Java;

public class UberX extends Car {

    String brand , model;

    public UberX(Integer id, String license, Account driver, String brand, String model) {
        super(id, license, driver);
        this.brand = brand;
        this.model = model;


    }
}
