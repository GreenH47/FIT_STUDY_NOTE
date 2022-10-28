/*
219×2=438
219×3=657
Now, concatenate the above results to the given number (n).
"219"+"438"+ "657"= 219438657 
it contains all the digit from 1 to 9, exactly once.
*/
import java.util.*;
public class SpecialNumber
{
   public static void main(String args[])
   {
        SpecialNumber objspecial = new SpecialNumber();
        int playernum = objspecial.checkNum();
        objspecial.specialCheck(playernum);
   }

   public int checkNum()
   {
        Scanner console = new Scanner(System.in);
        int playernum;
        String s;
        System.out.println("Enter number in 3 digits ");
        do
        { 
            try 
            {
                s = console.nextLine();
                playernum = Integer.parseInt(s);
                break;
            }
            catch (Exception e)//if no numeric warning
            {
                System.out.println("only Integer please try again");
            }
        }
        while (true);

        while(playernum > 999 || playernum < 100)
        {
            playernum = checkNum();//ask new number
        }
        return playernum;
   }

   public void specialCheck(int i)
   {
        int j = i * 2;
        int k = i * 3;
        String x = Integer.toString(i);
        String y = Integer.toString(j);
        String z = Integer.toString(k);
        x = x.concat(y);
        x = x.concat(z);
        char charArray[] = x.toCharArray();
        Arrays.sort(charArray);
        System.out.println("sorted Array : "+new String(charArray));
        
        String str = new String(charArray);
        int number = Integer.parseInt(str);
        int num = 123456789;
        if(number == num)
        {
            System.out.println(i+" is special number");
        }
        else
        {
            System.out.println(i+" not special number");
        }
   }
}//SpecialNumber.java
