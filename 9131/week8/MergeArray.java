/*
Write a program to randomly generate two Arrays, each containing 
random numbers between 1 and 50 (inclusive). The size of each array 
should also randomly be determined to be between 3 and 10 (inclusive). 
Then print both of these arrays on the screen. Then the program should 
combine both of these collections into a third array. However, 
the values in the third collection should be stored in ascending order 
(lowest to highest). Any duplicate numbers should not be added twice.
*/
import java.util.*;
public class MergeArray
{
   public static void main(String args[])
   {
        MergeArray objMerge = new MergeArray();
        int[] array1 = objMerge.generateArray();
        System.out.println("Array1 :"+Arrays.toString(array1));
        int[] array2 = objMerge.generateArray();
        System.out.println("Array2 :"+Arrays.toString(array2));
        int[] array3 = objMerge.mergeArray(array1, array2);
        System.out.println("Array merge :"+Arrays.toString(array3));
   }

   public int generateRandom(int min,int max)
   {
       int num = (int)(Math.random() * (max - min + 1) + min);
       return num;
   }

   public int[] generateArray()
   {
       int length = generateRandom(3,10);
       int[] arrayRandom = new int[length];
       int i;
       for(i = 0; i < arrayRandom.length; i++)
       {
           arrayRandom[i] = generateRandom(1,50);
       }
       return arrayRandom;
   }

   public int[] mergeArray(int[] array1, int[] array2)
   {
       Set<Integer> mergedSet = new HashSet<>();
       int i;
       int j = 0;
       for(i = 0; i < array1.length; i++)
       {
           mergedSet.add(array1[i]);
       }
       for(i = 0; i < array2.length; i++)
       {
           mergedSet.add(array2[i]);
       }

       int[] arraymerge = new int[mergedSet.size()];
       for(Integer k : mergedSet)
       {
           arraymerge[j++] = k;
       }
       Arrays.sort(arraymerge);
       return arraymerge;
   }

}//MergeArray.java
