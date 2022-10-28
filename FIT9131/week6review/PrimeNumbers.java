// store a set of prime numbers which are less than 1000
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PrimeNumbers
{
    public ArrayList<Integer> PrimesList;

    public PrimeNumbers()
    {
        primesList = new ArrayList<Integer>();
    }
    /*
    */
    //ArrayList<Integer> (An arraylist that will store all prime numbers <= maxNumber)
    public void primes(int n)
    {
        for (int x = 3; x < n; x++)
        {
             for (int i = 2; i < x; i++)
             {
                 if(x % i == 0)
                 {
                     primesList.add(x);
                 }
             }
        }

    }
    
    //: int (We will find all primes less than this number. 
    //For this exercise maxNumber should NOT exceed 1000)
    public int MaxNumber()
    {
        int n = PrimesList.size();
        int max = PrimesList.get(n-1);
        return max;
    }


    // accept a single integer parameter. Then using this paramete
    // find 5 prime numbers at that interval.
    //input 3 return 3, 6, 9, 12, 15
    //. Each number returned must be stored in the array. 
    //When the method finished print the primes in the array
    public void SequencePrimes()
    {
        Scanner conset = new Scanner(System.in);
        System.out.print("Enter find number: ");
        int x = conset.nextInt(); 
        int n = PrimesList.size();
        
        List<Integer> intValues = new ArrayList<>();
        for(int i=0; x<n-6; x++)
        {
            int finda = PrimesList.get(i);
            int findb = PrimesList.get(i+1);
            if((finda<x) &&(x<findb))
            {
                intValues.add(PrimesList.get(i+1));
                intValues.add(PrimesList.get(i+2));
                intValues.add(PrimesList.get(i+3));
                intValues.add(PrimesList.get(i+4));
                intValues.add(PrimesList.get(i+5));
            }
            
        }
        for (int i = 0; i < intValues.size();i++) 
	      { 		      
	          System.out.print(intValues.get(i)+", "); 		
	      }
    }


    //display the state of the object
    public void display()
    {   
        for (int i = 0; i < PrimesList.size();i++) 
	      { 		      
	          System.out.print(PrimesList.get(i)+", "); 		
	      }
    }

    public static void main(String[] args)
    {
        Scanner consle = new Scanner(System.in);
        System.out.print("Enter the array size: ");
        int num_input = consle.nextInt();
        PrimeNumbers primeNumber = new PrimeNumbers();
        primeNumber.primes(num_input);
        primeNumber.
    }
}
