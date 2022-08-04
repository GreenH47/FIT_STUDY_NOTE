import java.util.Arrays;
/**
You need to write a program to move all the 0’s to the end of the same array
*/

public class NineElements
{
    public void swapArray(int[] array,int i,int j)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public void moveZero(int[] array)
    {
        int i = 0;
        int j = 1;
        while(j < array.length)
        {
            if(array[i] == 0 && array[j] != 0)
            {
                swapArray(array,i,j);
                i++;
                j++;
            }
            else if(array[i] == 0 && array[j] == 0)
            {
                j++;
            }
            else
            {
                i++;
                j++;
            }
        }
    }
    
    public static void main(String[] args)
    {
        int[] arr = {0,8,0,4,3,0,6,0,2};
        NineElements nineElements = new NineElements();
        System.out.println("orignal array: ");
        System.out.println(Arrays.toString(arr));
        nineElements.moveZero(arr);
        System.out.println("change array: ");
        System.out.println(Arrays.toString(arr));

    }
}
