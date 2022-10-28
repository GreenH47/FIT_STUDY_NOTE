/*
You are required to write the code to read the one 
line of information provided and store each piece of data into a variable. 
You must use the substring() method in the String class to do this.
*/

import java.util.*;

public class DatatoVariable
{
    public static void main(String[] args)
    {
        String given = "Machu Picchu, Cuzco, Peru,1911";
        String name = "";
        String city = "";
        String country = "";
        int year = 0;

        String[] parts = given.split(",", 5);
        name = parts[0];
        city = parts[1];
        country = parts[2];
        year = Integer.valueOf( parts[3]);
        System.out.println(".split() method: "+ name + " " + city + " " + country + " " + year);

        name = given.substring(0,11);
        city = given.substring(14,19);
        country = given.substring(21,25);
        year = Integer.valueOf(given.substring(26,30));
        System.out.println(".substring() method: "+ name + " " + city + " " + country + " " + year);

    }
}//DatatoVariable.java
