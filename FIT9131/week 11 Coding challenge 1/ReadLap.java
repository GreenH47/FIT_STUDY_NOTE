import java.util.*;
import java.io.FileReader;

public class ReadLap
{
    public static void main(String[] args)
    {
        ReadLap objread = new ReadLap();
        
    }

    public static void readFile()
    {
        ArrayList<Lap> laps = new ArrayList<>();
        try{
            Scanner console = new Scanner(System.in);
            FileReader reader = new FileReader("lapTimes.txt");
            try{
                Scanner fileInput = new Scanner(reader);
                int counter = 0;
                while(fileInput.hasNextLine()){
                    counter++;
                    String[] lines = fileInput.nextLine().split(",");
                    String name = lines[0];

                    int age = 0;
                    try{
                        age = Integer.parseInt(lines[1]);
                    }catch(Exception e){
                        System.out.println("age Error");
                        continue;
                    }

                    double bestTime = 0.00;
                    try{
                        bestTime = Double.parseDouble(lines[2]);
                    }catch(Exception e){
                        System.out.println("bestTime Error");
                        continue;
                    }

                    double avgTime = 0.00;
                    try{
                        avgTime = Double.parseDouble(lines[3]);
                    }catch(Exception e){
                        System.out.println("avgTime Error");
                        continue;
                    }

                    int timeLength = lines.length - 4;
                    ArrayList<Double> averageLapTime = new  ArrayList<>();

                    for(int i = 0; i < timeLength;i++){
                        double recentTime = 0.00;
                        try{
                            recentTime  = Double.parseDouble(lines[i+4]);
                        }catch(Exception e){
                            System.out.println("recentTime  Error");
                            continue;
                        }
                        averageLapTime.add(recentTime);
                    }
                    laps.add(new Lap(name,age,bestTime,avgTime,averageLapTime));
                }
                for(Lap temp:laps)
                    System.out.println(temp.display());
            }finally{
                try{
                    reader.close();
                }catch(Exception e){
                    System.out.println("reading error");
                }
            }
        }catch(Exception e){
            System.out.println("writing error");
        }
    }
}//ReadLap.java
