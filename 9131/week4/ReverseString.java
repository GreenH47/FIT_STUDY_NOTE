/*
print the input string on the screen 
but in reverse order and in the reverse case.
*/

import java.util.Scanner;

public class ReverseString
{
    public static void main(String[] args)
    {
        String reverse_string ="";
        char string_char;
        Scanner console = new Scanner(System.in);
        System.out.println("string input? ");
        String input_string = console.nextLine();

        for (int i=0; i<input_string.length(); i++)
        {
            string_char = input_string.charAt(i);
            reverse_string = string_char + reverse_string;
        }
         System.out.print("Original word: "+input_string+"\n");
         System.out.print("Reversed word: "+ reverse_string+"\n");

    }
}
