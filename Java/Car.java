package Java;
import java.util.Scanner;

import static java.lang.System.exit;

public class Car {
    Integer id;
    String license;
    Account driver;
    Integer passenger, passenger_Limit;

    public Car(Integer id, String license, Account driver) {
        this.id = id;
        this.license = license;
        this.driver = driver;
        this.passenger_Limit = 4;
        this.passenger = 0;
    }

    void printData() {
        System.out.println("Car id: " + this.id);
        System.out.println("Car license: " + this.license);
        System.out.println("Car driver: " + this.driver.name);
        System.out.println("Car passengers: " + this.passenger);
        for (int i = 0; i < 20; i++) {
            System.out.print("-");
        }
        System.out.println();

    }

    void print_BasicData() {
        System.out.println("Car driver: " + this.driver);
        System.out.println("Car license: " + this.license);
    }

    void print_Passenger() {
        System.out.printf("Your car have %d a  passengers: ", this.passenger);
    }

    void setPassenger() {
        Scanner in = new Scanner(System.in);
        int passenger_in;
        System.out.print("Enter the number of passengers: ");
        passenger_in = in.nextInt();

        if (passenger_in > this.passenger_Limit) {
            System.out.println("You can't add more passengers");
            System.out.println("The limit of passengers is: " + this.passenger_Limit);
            exit(0);
        } else {
            this.passenger = passenger_in;
        }
    }



}
