/**
 Class that allows us to accept some basic input 
 from the user using the Scanner class
 */
 
/*
This import is necessary as the Scanner class 
is not automatically included when we write our programs
*/
import java.util.Scanner;

public class ScannerExample
{
    public ScannerExample()
    {
        //Empty Constructor as we do not have fields
    }
    
    /*
      Main method to run the program
     */
    public static void main(String[] args)
    {
        ScannerExample scanner = new ScannerExample();
        scanner.testScanner();
    }
    
    /*
      Method that allows us to accept input using the Scanner class
     */
    public void testScanner()
    {
        int age;
        char status;
        String name;
        
        //Here we are creating an object of the Scanner class
        //What do you think System.in is referring to? If unsure, ask your teaching staff.
        Scanner console = new Scanner(System.in);
        
        System.out.println("Welcome to the Scanner example!");
        System.out.print("Press enter to continue ... ");
        
        //The nextLine() method reads everything on a single line until the enter key
        //Why do you think we are not storing the value in some variable?
        console.nextLine();
        
        System.out.print("Enter your name: ");
        name = console.nextLine();
        System.out.println("Hello, " + name);
        
        System.out.print("Postgrad or Undergrad - P/U: ");
        
        //When we use nextLine() method we get the input entered as a string.
        //So when we now call the charAt() method, which class do you think this belongs to?
        //Find the class and read the documentation to understand how this method works.
        status = console.nextLine().charAt(0);
        System.out.println("Your status is " + status);
        
        System.out.print("Enter your age: ");
        
        //The scanner class allows us to accept specific data type inputs.
        //What specific data type input do you think nextInt() will accept?
        //Try passing in some arbitrary value here, what do you think happens?
        age = console.nextInt();
        System.out.println("Your age is " + age);    
    }
}
