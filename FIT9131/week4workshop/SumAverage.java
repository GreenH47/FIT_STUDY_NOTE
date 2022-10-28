import java.util.Scanner;
/*
Write a program that reads ten integers from the keyboard 
and calculates their sum and average, then prints these values to the screen.
*/
public class SumAverage
{
    public static void main(String[] args)
    {
        // array size input
        Scanner consle = new Scanner(System.in);
        System.out.print("Enter the array size: ");
        int arr_len = consle.nextInt();
        int arr[] = new int[arr_len];
        double num_sum = 0;
        double num_avg = 0;

        //input the array number and calculates their sum
        System.out.println("Enter the  array element");
        for (int i=0;i<arr_len;i++)
        {
            arr[i] = consle.nextInt();
            num_sum += arr[i];
        }

        num_avg = num_sum/arr_len;
        System.out.println("Sum of "+arr_len+" number in "+num_sum);
        System.out.println("Average is "+num_avg);

    }
}
