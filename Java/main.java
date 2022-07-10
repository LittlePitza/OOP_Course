package Java;

class main {
    public static void main(String[] args) {

        System.out.println("Hello, World!");

        Car car = new Car();
        car.id = 1;
        car.license = "ABC-123";
        car.driver = "John";
        car.passenger = 4;

        car.printData();

        // Making other car

        System.out.println("Other car");

        Car car2 = new Car();

        car2.id = 2;
        car2.license = "XYZ-456";
        car2.driver = "Tom";
        car2.passenger = 2;

        car2.print_BasicData();
        car2.print_Passenger();






    }
}