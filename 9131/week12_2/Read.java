import java.io.FileReader;
import java.util.*;
/*
You have been provided with a text file in the workspace window called "todolist.txt".

This file contains data in the following format:

priority, task name, task description, task owner
You are required to write the program to read this information from the file, store it in an appropriate collection, and display it on the screen.

Your program must report exceptions only.

You may include any additional classes based on responsibility driven design and if included each class must include all the required aspects such as constructors, accessors, mutators, and a display method.
*/
public class Read
{
    public static void main(String[] args)
    {
        ArrayList<Task> taskList = new ArrayList<>();
        try
        {
            FileReader reader = new FileReader("todolist.txt");
            Scanner getFile = new Scanner(reader);
            while(getFile.hasNextLine())
            {
                String[] arrayRow = getFile.nextLine().split(",");
                Task temp = new Task(arrayRow[0],arrayRow[1],arrayRow[2],arrayRow[3]);
                taskList.add(temp);
                System.out.println(temp.display());
            }
            reader.close();
        }
        catch(Exception e)
        {
            System.out.println("file not found");
        }
        
    }
}//Read.java
