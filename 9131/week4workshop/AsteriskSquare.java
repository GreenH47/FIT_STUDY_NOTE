import java.util.Scanner;
/*
accepts an integer, n, 
and prints to the screen an n x n square of asterisks,
*/
public class AsteriskSquare
{
    public static void printSquare(int n)
    {
        // print the square
        for(int i = 0; i < n;i++)
        {
            for(int j = 0; j < n;j++)
            {
                System.out.print("*");
            }
            System.out.println("");
        }
    }


    public static void main(String[] args)
    {
        System.out.println("Enter a value: ");
        Scanner console = new Scanner(System.in);
        printSquare(console.nextInt());
    }
}
