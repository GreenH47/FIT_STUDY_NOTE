import java.util.Scanner;

public class Permutation
{
    public static void printString(String input)
    {
        int length = input.length();
        int flag = 1;
        int i,j,k;
        for(i = 0; i < length;i++)
        {
            for(j = 0; j < length;j++)
            {
                for(k = 0; k < length;k++)
                {
                    flag++;
                    System.out.println(flag + ": "+input.charAt(i)+""+input.charAt(j)+""+input.charAt(k));
                }
            }
        }
    }

    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);
        String input = "";
        while(input.length() != 3)
        {
            System.out.println("plz input 3 letter: ");
            input = console.nextLine();
        }
        printString(input);
    }//Permutation.java
}
