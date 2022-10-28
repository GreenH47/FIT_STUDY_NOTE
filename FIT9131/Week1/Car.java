public class Car
{
    private String make;
    private String model;
    private int year;
    private String color;

    public Car()
    {
        make = "Unknown";
        model = "Unknown";
        year = 1900;
        color = "Unknown";
    }

    public Car(String newMake, String newModel, int newYear, String newColor)
    {
        make = newMake;
        model = newModel;
        year = newYear;
        color = newColor;
    }

    public static void main(String[] args)
    {
        Car objCar = new Car("Toyota", "Corolla", 2018, "Blue");
        objCar.setColor("Yellow");
        System.out.println("The color of the car is: " + objCar.getColor());
    }

    public String getColor()
    {
        return color;
    }

    public void setColor(String color)
    {
        color = color;
    }    
}
