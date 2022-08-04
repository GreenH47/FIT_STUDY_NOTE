




public class Selection1 
{
    
    public static void main(String[] args)
    {
        char seatLocation = 'B';
        int price = 0;
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
            default: 
                System.out.println("Unknown seat location"); 
                price = 0; 
                break;
        }
        System.out.println(price);
    }

}

