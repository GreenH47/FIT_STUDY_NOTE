import java.util.Scanner;
    
    public class HelloWorld
    {
       private String name;
       
       public HelloWorld()
       {
           name = "No one";
       }
       
       public HelloWorld(String newName)
       {
           name = newName;
       }
       
       public static void main(String[] args)
       {
           HelloWorld hw = new HelloWorld();
           hw.startProgram();
       }
       
       public void startProgram()
       {
           Scanner console = new Scanner(System.in);
           System.out.println("Please enter your name");
           String tempName = console.nextLine();
           if (tempName.trim().length() > 0)
               name = tempName;
           System.out.println("Welcome " + name);
       }
    }
