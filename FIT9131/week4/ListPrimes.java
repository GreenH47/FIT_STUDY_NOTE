/*
ask the user for an integer input. 
Based on the input, the method must 
print out all the prime numbers less than that number.
*/

import java.util.Scanner;
public class ListPrimes
{
    static void primenumber(int MyNum) 
    {
        int n = 0;
        for(int i = 2; i < (MyNum/2+1); i++) 
        {
            if(MyNum % i == 0)
            {
                n++;
                break;
            }
        }

        if (n == 0)
        {
            System.out.print(MyNum + " ");
        } 
    }

    public static void main(String[] args) 
    {
        Scanner console = new Scanner(System.in);
        System.out.println("What number? ");
        int x = console.nextInt();
        System.out.println("Prime numbers less than "+ x + " are: ");
        for(int i = 2; i < x + 1; i++) 
        {
            primenumber(i);
        }
    }
}
