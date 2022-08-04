import java.util.*;
/*
Write a program to accept two inputs from the user through the keyboard:

a single character (this can be a letter, number or symbol)

a number to represent a level that must be between 5 and 10 inclusive. 

Based on the above choices, the system will generate a pattern to be displayed on the screen as shown below:


For the above example, the character entered is * and the number of levels is 5. 

The patterns must be displayed using the input characters specified by the user and the number of levels should be determined based on the value entered by the user.

You must validate the required inputs mentioned above and ensure that inputs must not contain only spaces or be empty.

In the above process, make sure you check if the user input is within the range. And your code should be reusable. You must use for, while or do-while for your main logic and your code should be reusable.
*/
public class DiamondPattern
{
    public static void main(String[] args)
    {
        DiamondPattern diamondPattern = new DiamondPattern();
        diamondPattern.start();
    }

    public void start()
    {
        System.out.println("Enter a character: ");
        Scanner console = new Scanner(System.in);
        String character = console.nextLine();
        char temp = character.charAt(0);
        String symbol = String.valueOf(temp); 

        System.out.println("level(5~10)? ");
        int level = console.nextInt();
        while(level < 5 || level >10)
        {
            System.out.println("level(5~10)? ");
            level = console.nextInt();
        }
        printSquare(symbol,level);
    }

    public void printSquare(String symbol,int level)
    {
        for(int i = 1; i <=level;i++)
        {
            String space = "";
            String charstr = "";
            if(level - i == 0)
            {
                for(int k = 1; k < i*2 ; k++)
                {
                    charstr = charstr + symbol; 
                }
                System.out.println(space + charstr + space);
                continue;
            }
            for(int j = 0; j<(level-i);j++)
            {
                space = space + " ";
            }
            
            for(int k = 1; k < i*2 ; k++)
            {
                charstr = charstr + symbol; 
            }
            System.out.println(space + charstr + space);
        }


        for(int i = 1; i < level;i++)
        {
            String space = "";
            for(int j = 0; j<i ;j++)
            {
                space = space + " ";
            }

            String charstr = "";
            for(int k = (level - i)*2; k > 1 ; k--)
            {
                charstr = charstr + symbol; 
            }
            System.out.println(space + charstr + space);
        }
    }


}//DiamondPattern.java
