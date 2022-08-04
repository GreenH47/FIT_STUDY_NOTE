import java.util.Scanner;
import java.util.ArrayList;


/**
 * A class to define a constructure to store person name and age
 */
public class AgeDatabase
{
    public ArrayList<PersonAge> entries;

    public AgeDatabase()
    {
        entries = new ArrayList<PersonAge>();
    }

    /**
     * Method that add a new person into database
     * @param name An integer value representing starting amount
     * @param age An integer value representing time 
     */
    public void addNew(String name, int age)
    {
        PersonAge entry = new PersonAge(name, age);
        entries.add(entry);
    }

    public void display()
    {   
        for (PersonAge entry : entries)
        {
            System.out.println("Name: " + entry.getName() + ", Age: " + entry.getAge());
        }
    }

    public PersonAge getYoungest()
    {
        PersonAge min = entries.get(0);
        for (PersonAge e : entries)
        {
            if (e.getAge() < min.getAge())
            {
                min = e;
            }
        }
        return min;
    }

    public PersonAge Old()
    {
        PersonAge max = entries.get(0);
        for (PersonAge e : entries)
        {
            if (e.getAge() > max.getAge())
            {
                max = e;
            }  
        }
        return max;
    }

    public static void main(String[] args)
    {
        int opt = 0;
        AgeDatabase db = new AgeDatabase();
        Scanner console = new Scanner(System.in);

        do
        {
            System.out.println("Enter 1 to store a new name and age in the database.");
            System.out.println("Enter 2 to print all names and ages.");
            System.out.println("Enter 3 to print the youngest person.");
            System.out.println("Enter 4 to print the oldest person.");
            System.out.println("Enter 5 to quit the program.");

            opt = Integer.parseInt(console.nextLine());

            switch (opt)
            {
                case 1:
                    System.out.println("Enter name:");
                    String name = console.nextLine();
                    System.out.println("Enter age:");
                    int age = Integer.parseInt(console.nextLine());
                    db.addNew(name, age);
                    break;
                case 2:
                    db.display();
                    break;
                case 3:
                    db.getYoungest().display();
                    break;
                case 4:
                    db.Old().display();
                case 5:
                    break;
                default:
                    System.out.println("Not a valid menu choice.");
            }

        } while (opt != 5);
    }
}


