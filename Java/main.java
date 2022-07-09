package Java;

class main {
    public static void main(String[] args) {

        System.out.println("Hello, World!");

        Car car = new Car();
        car.id = 1;
        car.license = "ABC-123";
        car.driver = "John";
        car.passenger = 4;

        System.out.println("Car id: " + car.id);
        System.out.println("Car license: " + car.license);
        System.out.println("Car driver: " + car.driver);
        System.out.println("Car passengers: " + car.passenger);



    }
}