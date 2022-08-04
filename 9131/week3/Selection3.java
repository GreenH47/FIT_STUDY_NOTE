public class Selection3
{
    public static void main(String[] args)
    {
        int amount = 0;
        int balance = 50;
        if (amount >= 0) 
        {
            balance = balance + amount;
            System.out.println(balance);
        }
        else
            System.out.println("Invalid amount:  " + amount);
    }

}

