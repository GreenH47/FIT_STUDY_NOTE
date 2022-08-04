import java.util.Scanner;
public class Selection2
{
    
    public static void main(String[] args)
    {
        char seatLocation;
        int price;
        Scanner console = new Scanner(System.in);
        System.out.print("Enter seat Location: ");
        seatLocation = console.nextLine().charAt(0);
        switch (seatLocation)
        {
            case 'A': 
                System.out.println("Front row"); 
                price = 100; 
                break;
            case 'B': 
                System.out.println("Stalls"); 
                price = 80; 
                break;
            case 'C': 
                System.out.println("Balcony"); 
                price = 55;
                break;
            default: 
                System.out.println("Unknown seat location"); 
                price = 0; 
                break;
        }
        System.out.println(price);
    }

}

