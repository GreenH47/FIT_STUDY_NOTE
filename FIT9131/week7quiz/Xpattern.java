import java.util.Scanner;

public class Xpattern
{
    public void drawPattern()
    {
        int playernum = checkNum();
        System.out.println("==============");
        int i,j;
        String side;
        String mid;
        for(i = 1; i < playernum; i++)//up part
        {
            side = "";
            for(j = playernum - i; j < playernum; j++)
            {
                side += " ";
            }
            mid = "";
            for(j = i; j < playernum - 1; j++)
            {
                mid += "  ";
            }
            System.out.println(side+"" + i +""+ mid +""+ i +""+ side);
        }

        String space = "";//mid part
        for(i = 1; i < playernum; i++)
        {
            space += " ";
        }
        System.out.println(space+"" + playernum +""+ space);

        //down part
        for(i = playernum -1; i > 0; i--)//up part
        {
            side = "";
            for(j = playernum - i; j < playernum - 1; j++)
            {
                side += " ";
            }
            mid = "";
            for(j = i; j < playernum - 1; j++)
            {
                mid += "  ";
            }
            System.out.println(side+"" + i +""+ mid +""+ i +""+ side);
        }
    }

    public int checkNum()
    {
        Scanner console = new Scanner(System.in);
        int playernum;
        String s;
        System.out.println("Enter number in [4,10] ");
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

        while(playernum > 10 || playernum < 4)
        {
            playernum = checkNum();//ask new number
        }
        return playernum;
    }

    public static void main(String[] args)
    {
        Xpattern objdisplay = new Xpattern();
        objdisplay.drawPattern();
    }
}//Xpattern.java
