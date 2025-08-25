public class FeverChecker {
    public static void main(String[] args) {
        double temperature = 101.5; // Replace this with the temperature you want to check
        
        if (isFever(temperature)) {
            System.out.println("The temperature (" + temperature + "°F) indicates a fever.");
        } else {
            System.out.println("The temperature (" + temperature + "°F) is not indicative of a fever.");
        }
    }
    
    public static boolean isFever(double temperature) {
        return temperature > 100.0;
    }
}
