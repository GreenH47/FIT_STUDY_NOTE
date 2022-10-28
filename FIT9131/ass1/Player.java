import java.util.Scanner;
import java.util.Random;
import java.lang.Math;
/**
 * Class which The Player class will specify 
 *the attributes and behaviours of a player.
 *
 */

public class Player
{

    //Fields
    private String name;
    private int guess;
    private int score;

   /**
    * Default constructor which creates the object of the class Player.
    *
    */
    public Player()
    {
        name = "";
        guess = 0;
        score = 0;
    }
    
    /*
     * Non-Default constructor which creates the object of the class Player.
     *
     * @param newName     Accepts the user name as a string.
     * @param newGuess    Accepts the player new guess number as a int.
     * @param newScore    Accepts the player score as a int.
     */
    public Player(String newName,int newGuess,int newScore)
    {
        this.name = newName;
        this.guess = newGuess;
        this.score = newScore;
    }

    /**
     * Accessor method to get player name.
     *
     * @return              The player name as a String.
     */
    public String getName()
    {
        return this.name;
    }
    /**
     * Mutator method to check player name validation and store.
     *
     * @param   newName  The player name as a String.
     */
    public void setName(String newName)
    {
        while(newName.length() > 8)//this loop makes sure input name length <= 8
        {
            Scanner set = new Scanner(System.in);
            System.out.println("user name no more than 8 characters: ");
            newName = set.nextLine();
        }
        this.name = newName;
    }

    /**
     * Accessor method to get player guess number.
     *
     * @return              The player guess number as a int.
     */
    public int getGuess()
    {
        return this.guess;
    }
    /**
     * Mutator method to set player guess number.
     *
     * @param   newName  The player name as a String.
     */
    public void setGuess(int newGuess)
    {
        this.guess = newGuess;
    }

    /**
     * Accessor method to get player score total.
     *
     * @return              The player score as a int.
     */
    public int getScore()
    {
        return this.score;
    }
    /**
     * Mutator method to add player guess number.
     *
     * @param   newScore  The player score get this round as a int.
     */
    public void setScore(int newScore)
    {
        //add score for one turn
        this.score = this.score + newScore;
    }

    /**
     * Formats the state of the player 
     *
     * @return           The state of the player as a string.
     */
    public String display()
    {
        String nameState = "player name: " + this.name;
        String guessState = "; last guessed this round: " + this.guess;
        String scoreState = "; game score total: " + this.score;
        return nameState + guessState + scoreState;
    }

    //Player.java

}
