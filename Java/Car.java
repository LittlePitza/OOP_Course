package Java;

public class Car {
    Integer id;
    String license;
    public String driver;
    Integer passenger;

    void printData() {
        System.out.println("Car id: " + id);
        System.out.println("Car license: " + license);
        System.out.println("Car driver: " + driver);
        System.out.println("Car passengers: " + passenger);
    }

    void print_BasicData() {
        System.out.println("Car driver: " + driver);
        System.out.println("Car license: " + license);
    }

    void print_Passenger() {
        System.out.printf("Your car have %d a  passengers: ", passenger);
    }



}
