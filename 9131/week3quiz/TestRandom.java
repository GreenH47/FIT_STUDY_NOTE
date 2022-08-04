import java.util.Random;
import java.util.Scanner;

/*
The program will generate two random numbers 
by using RNG class object between 10 and 20 
and display the addition and multiplication of two random numbers
*/
public class TestRandom
{
    public static void main(String[] args)
    {
        Random random = new Random();
        int ran_n1 = random.nextInt(10) + 10;
        int ran_n2 = random.nextInt(10) + 10;
        System.out.println ("randomNumber is  "+ran_n1
                            +" and "+ran_n2) ; 
        
        int add_num = ran_n1 + ran_n2;
        int mul_num = ran_n1 * ran_n2;
        System.out.println ("the addition is  "+add_num
                            +" and multiplication "+mul_num) ; 

    }
}

