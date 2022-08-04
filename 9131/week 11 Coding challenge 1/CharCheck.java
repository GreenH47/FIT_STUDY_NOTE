import java.util.*;
/*
Write a program that accepts a string input from the user via the keyboard. The program then prompts the user for another input, which must be a single character. The program will then check how many times the second input occurs in the first. It will then print out the number of times it appears and the index in the string for each occurrence. An example has been shown below:

Please enter a string: Hello World. There is sunshine here! Please enter a single character: E e appears in hello world. there is sunshine here at index (es): 2, 16, 18, 30, 33, 35
Please note the searches and inputs are all case-insensitive!
*/
public class CharCheck
{
    public static void main(String[] args)
    {
        System.out.println("String input: ");
        Scanner console = new Scanner(System.in);
        String inputString = console.nextLine();

        System.out.println("Char input: ");
        char inputChar = console.nextLine().toLowerCase().charAt(0);

        int times = 0;
        int i = 0;
        ArrayList<Integer> index = new ArrayList<>();

        for(i = 0; i < inputString.length();i++)
        {
            if(inputChar == inputString.toLowerCase().charAt(i))
            {
                times++;
                index.add(i);
            }
        }

        System.out.println(inputChar+" appears " + times + " times in " + inputString);
        System.out.println("Char At index: "+index.toString());
    }
}//CharCheck.java
