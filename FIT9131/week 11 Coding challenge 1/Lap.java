import java.util.*;
/*
You have been provided with a text file "lapTimes.txt". The file contains information for various runners and details about their lap times in a 400m race track. The data given in the file is accurate but not all the recent laps have been recorded for all the runers. The details stored are as follows:

Name - String

Age - int

Best Lap Time - double

Average Lap Time - double

Recent Lap Times - double.

The recent lap times are based on the runners and the number of laps that have been recorded. The maximum is 5 recent laps. Some might have fewer or even none.

Write a program to read this information from the provided file and display it on the screen.

You should apply the concepts we have learned so far, including responsibility-driven design, high cohesion and low coupling, exception handling, validations, and overall good code structure, to name a few. A more scalable design will be considered to be a better design.
*/
public class Lap
{
    private String name;
    private int age;
    private double bestLapTime;
    private double averageLapTime;
    private ArrayList<Double> recentLapTime;

    public Lap()
    {
        this.name = "";
        this.age = 0;
        this.bestLapTime = 0.00;
        this.averageLapTime = 0.00;
        this.recentLapTime = new ArrayList<>();
    }

    public Lap(String name,int age,double bestLapTime,double averageLapTime,ArrayList<Double> recentLapTime)
    {
        this.name = name;
        this.age = age;
        this.bestLapTime = bestLapTime;
        this.averageLapTime = averageLapTime;
        this.recentLapTime = recentLapTime;
    }

    public String display()
    {
        return name + age + bestLapTime + averageLapTime + recentLapTime;
    }
}//Lap.java
