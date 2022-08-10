
import java.util.Scanner;
import java.util.Random;
import java.lang.Math;
/**
 * Class which  generate a random number from 1 to a maximum value specified.
 *
 */

public class NumberGenerator
{
    
    /**
    * generate random int number in range 1 to max
    *@param max    the max number of the generate range
    *@return       random int number bewteen 1 and max
    */
    public int generateRandomNumber(int max)
    {
        //generate random int number in [1,max+1)
        int randomNumber = (int)(Math.random() * max) + 1;
        return randomNumber;
    }

}
