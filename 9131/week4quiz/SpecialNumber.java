/*
A number will be a special number
 only if the sum and product of all digits are equal. 
 Hence 132 is a special number
*/

import java.util.Scanner;

public class SpecialNumber
{
    public static void numbercheck(int num)
    {
        int check = num;
        int count = 0;
        int digit = 0;
        int digit_sum = 0;
        int digit_product = 1;
        while (check!= 0)
        {
            digit = check % 10;
            check /= 10;
            digit_sum += digit;
            digit_product *= digit;
            count++;
        }

        if (count < 2)
            System.out.println("number need at least 2-digit ");
        else if (digit_sum == digit_product)
            System.out.println(num +"is special number");
        else
            System.out.println(num +" is not special number");
    }

    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);
        System.out.println("plz enter number");
        int input_number = console.nextInt();
        numbercheck(input_number);

    }
}
