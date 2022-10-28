/*
Write a program to accept two inputs from the user through the keyboard:

a single character (this can be a letter, number or symbol)

a string of any length

The program then returns the String after removing the single character input by the user and its immediate left and right characters. An example has been shown below:

Sample Output:

User Input(String): test#string

User Input(Character): #

Output should be: testring
*/
import java.util.*;

public class RemoveCharacter
{
    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);
        System.out.println("input string:");
        String inputStr = console.nextLine();

        System.out.println("input char:");
        String inputChar = console.nextLine();

        int year = inputStr.indexOf(inputChar);
        String result = inputStr.replace(inputStr.substring(year-1,year+2),"");
        System.out.println(result);
    }
}//RemoveCharacter.java
