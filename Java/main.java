package Java;

class main {
    public static void main(String[] args) {

        System.out.println("Hello, World!");

        Car car = new Car(1, "ABC-1234", new Account("Pizza", "123.6.789-00"));
        Car car2 = new Car(2, "ABC-1235", new Account("Marian", "123.46.789-00"));
        Car car3 = new Car(3, "ABC-1236", new Account("Alex", "123.456.3-00"));

        car.printData();
        car.setPassenger();
        car.printData();
        car2.printData();
        car3.printData();







    }
}