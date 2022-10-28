import java.math.BigDecimal;
import java.util.Scanner;
/**
find roots of quadratic equation 
*/
public class Quadratic
{
    public static void main(String[] args)
    {
        double root1,root2;
        Scanner console = new Scanner(System.in);
        System.out.println("plz enter a");
        double a = console.nextDouble();

        System.out.println("plz enter b");
        double b = console.nextDouble();

        System.out.println("plz enter c");
        double c = console.nextDouble();

        double d = Math.pow(b,2) - 4 * a * c;

        if(d > 0)
        {
            root1 = ((-b) + Math.sqrt(d))/(2 * a);
            root2 = ((-b) - Math.sqrt(d))/(2 * a);
            System.out.println("root1 = "+ String.format("%.2f", root1));
            System.out.println("root2 = "+ String.format("%.2f", root2));
        }

        else if(d == 0)
        {
            root1 = (-b)/(2*a);
            System.out.println("root1 = root2 = "+ String.format("%.2f", root1));
        }

        else if(d < 0)
        {
            double real,imaginary;
            real = (-b)/(2*a);
            imaginary = Math.sqrt(-d)/(2 * a);
            System.out.println("root1 = " + String.format("%.2f", real) + " + " +String.format("%.2f", imaginary) + "i");
            System.out.println("root1 = " + String.format("%.2f", real) + " - " +String.format("%.2f", imaginary) + "i");
        }

    }
}
