import java.util.Scanner;

//read each of the numbers 
//and then calculate the sum based on the following formula

public class Code
{
    //determine if a number is divisible by 5.
    public static int getChange(int day)
    {
        int change_num = 0;
        switch (day%5)
        {
            case 0:
                change_num = day/5;
                break;
            default:
                change_num = day*5;
                break;
        }
        return change_num;
    }

    public static void main(String[] args)
    {
        //get input and display
        Scanner console = new Scanner(System.in);
        System.out.println("Please enter numbers");
        int num1 = console.nextInt();
        int num2 = console.nextInt();
        int num3 = console.nextInt();
        System.out.println("number is "+num1+" and "+num2+" and "+num3);

        //change the input number and display
        int chang1 = getChange(num1);
        int chang2 = getChange(num2);
        int chang3 = getChange(num3);
        System.out.println("change is "+chang1+" and "+chang2+" and "+chang3);
        
        //calculate the sum based on the following formula. 
        double total = chang1 +chang2 +chang3;
        System.out.println("the total is : " + String.format("%.2f", total));
    }
}

