
//generate a random number between a minimum and maximum specified by the user. 
import java.util.Random;
import java.util.Scanner;

public class RNG
{
    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);
        System.out.println("minimum ");
        int Min = Integer.parseInt(console.nextLine());

        System.out.println("maximum  ");
        int Max = Integer.parseInt(console.nextLine());

        Random random = new Random();
        int randomNumber = random.nextInt(Max) + Min;
        System.out.println ("randomNumber is  "+randomNumber) ; 
    }
}

