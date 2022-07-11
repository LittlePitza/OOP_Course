package Java;
import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends UberX {

    Map<String, Map<String, Integer>> typeCarAccepted;

    public UberBlack(Integer id, String license, Account driver, String brand, String model) {
        super(id, license, driver, brand, model);
    }
}
