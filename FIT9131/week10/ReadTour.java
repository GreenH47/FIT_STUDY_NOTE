import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class ReadTour
{
    public static void main(String[] args)
    {
        ArrayList<Tour> tours = new ArrayList<>();

        try
        {
            Scanner console = new Scanner(System.in);
            FileReader reader = new FileReader("tours.txt");

            try
            {
                Scanner fileInput = new Scanner(reader);
                while(fileInput.hasNextLine())
                {
                    String[] lineContents = fileInput.nextLine().split(",");
                    String origin = lineContents[0];
                    String destination = lineContents[1];

                    int days = 0;
                    try
                    {
                        days =  Integer.parseInt(lineContents[2]);
                    }
                    catch(Exception e)
                    {
                        System.out.println("Days Error");
                        continue;
                    }

                    int cost = 0;
                    try
                    {
                        cost =  Integer.parseInt(lineContents[3]);
                    }
                    catch(Exception e)
                    {
                        System.out.println("costs Error");
                        continue;
                    }

                    tours.add(new Tour(origin,destination,days,cost));

                }
                for(Tour temp : tours)
                    System.out.println(temp.display());
            }
            finally
            {
                try
                {
                    reader.close();
                }
                catch(Exception e)
                {
                    System.out.println("File can not read!");
                }
            }
        }
        catch(Exception e)
        {
            System.out.println("File can not write!");
        }
    }
}//ReadTour.java
