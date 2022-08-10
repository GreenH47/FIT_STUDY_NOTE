import java.util.Scanner;
import java.util.Random;
import java.lang.Math;
/**
 * Class which The Game class will manage the playing of a game
 */
public class Game
{
    //Initialize Fields here
    private NumberGenerator numberGenerator;
    private Player player1;
    private Player player2;

    /**
     * Default constructor which creates the object of the class Game.
     *
     */
    public Game()
    {
        numberGenerator = new NumberGenerator();
        //public Player(String newName,int newGuess,int newScore)
        player1 = new Player("",0,0);
        player2 = new Player("",0,0);
    }
    
    /*
     * Non-Default constructor which creates the object of the class Game.
     *
     * @param player1          Accepts the Player as player1.
     * @param player2           Accepts the Player as player2.
     * @param numberGenerator    Accepts the NumberGenerator as numberGenerator.
     */
    public Game(Player player1,Player player2,NumberGenerator numberGenerator)
    {
        this.player1 = player1;
        this.player2 = player2;
        this.numberGenerator = numberGenerator;
    }

    /**
     * Accessor method to get the player1.
     *
     * @return              player1 state .
     */
    public Player getPlayer1()
    {
        return this.player1;
    }
    
    /**
     * Accessor method to get the player2.
     *
     * @return              player2 state .
     */
    public Player getPlayer2()
    {
        return this.player2;
    }

    /**
     *  method to check which guess closer and get +1 score
     *
     * @param guess         hidden guess number as a int.
     * @param oneguess      player1 guess number as a int.
     * @param twoguess      player2 guess number as a int.
     * @return              who is winner of this round as display.
     */
    public void closeNumber(int guess,int oneguess,int twoguess)
    {
        System.out.println("guess number is: "+guess);//print guess number
        //Compare which is closer
        if (Math.abs(oneguess-guess) < Math.abs(twoguess-guess)) 
        {
            //player1 closer get 1 point
            System.out.println(player1.getName()+" number is closer get 1 point this round");
            player1.setScore(1);//store 1p score
        } 
        else if(Math.abs(oneguess-guess) > Math.abs(twoguess-guess))
        {
            //player2 closer get 1 point
            System.out.println(player2.getName()+ " number is closer get 1 point this round");
            player2.setScore(1);//store 2p score
        }
        else
        {
            System.out.println("computer and player all closer none get points");
        }
    }
    
    /**
     *  method to generate computer guess number
     *
     * @param low         generate number low range as a int.
     * @param high        generate number high range as a int.
     * @return  guess     computer guess number as int.
     */
    public int computerGuess(int low, int high)
    {
        //generate random in range[low,high]
        int remain = high - low;
        int guess = numberGenerator.generateRandomNumber(remain) + low;
        //check if skip
        int skip = numberGenerator.generateRandomNumber(20);
        if(skip == 20)//5% chance to give up round
        {
            guess = 999;
        }
        System.out.println(" computer guess number: " + guess );
        return guess;
    }

    /**
     *  method to check which player has more score
     *
     * @return         who is winner of this game as display.
     */
    public void gameEnd()
    {
        //this condition computer score and print winner
        if(player1.getScore() < player2.getScore())//player2 more score!
        {
            System.out.println(player2.getName()+" is winner!");
        }

        else if(player1.getScore() > player2.getScore())//player1 more score!
        {
            System.out.println(player1.getName()+" is winner!");
        }

        else//same score
        {
            System.out.println("player and computer both winner!");
        }
        System.out.println("======================");
        System.out.println("game end!");
    }//Game.java

    /**
     *  method to start one round, check number, check & store score , display result
     *@param    mode          An int to select player1 is human or computer.
     * @return              The state of the player as display.
     */
    public void gameStart(int mode)
    {
        
        int guess = numberGuess();//generate guess number
        
        boolean onegiveup = false;//player1 giveup flag
        boolean twogiveup = false;//player2 giveup flag
        int attempt = 0;//how many attempt
        int high = 101;//set high range
        int low = 0;//set low range
        int oneguess = 1;
        int twoguess = 1;
        while (attempt < 6)//this loop check anyone correct or attempt reach 6
        {
            if(mode ==1)
            {
                oneguess = humanGuess(low + 1,high - 1);//mode1 player1 is human guess number
            }
            else
            {
                oneguess = computerGuess(low + 1,high - 1);//mode2 player1 is computer guess number
            }
            
            attempt++;
            if(oneguess == guess)//player1 guess correct
            {
                break;
            }
            if(oneguess == 999)//player1 give up
            {
                onegiveup = true;
                break;
            }


            if(oneguess >= low && oneguess <= high)//player1 number in range
            {
                if(guess < oneguess)//player1 num high than guess
                {
                    System.out.println("number are higher than guess number");//print higher message
                    if(high > oneguess)//check if range smaller
                    {
                        high = oneguess;//set new high range
                    }
                }
                else//player1 num low than guess
                {
                    System.out.println("number are lower than guess number");//print lower message
                    if(low < oneguess)//check if range smaller
                    {
                        low = oneguess;//set new low range
                    }
                }
            }

            if(mode ==1)
            {
                twoguess = computerGuess(low + 1,high - 1);//mode1 player2 is computer guess number
            }
            else
            {
                twoguess = humanGuess(low + 1,high - 1);//mode2 player2 is human guess number
            }
            attempt++;
            if(twoguess == guess)//player2 correct
            {
                break;
            }
            if(twoguess == 999)//player2 give up
            {
                twogiveup = true;
                break;
            }

            if(guess < twoguess)//player2 num high than guess
            {
                System.out.println("number are higher than guess number");//print higher message
                if(twoguess < high)//check if range smaller
                {
                    high = twoguess;//set new high range
                }
            }
            else//pplayer2 num lower than guess
            {
                System.out.println("number are lower than guess number");//print lower message
                if(twoguess > low)//check if range smaller
                {
                    low = twoguess;//set new low range
                }
            }


        }
        //check one round score
        if(attempt == 6 && oneguess != guess && twoguess != guess )//turn 6 none win check closer
        {
            if(!onegiveup && !twogiveup)
            {
                closeNumber(guess,oneguess,twoguess);//check store and display sccore and winner
            }
        }
        else
        {
            playerScore(attempt,onegiveup,twogiveup);//someone number correct or give up
        }
        
        //display player state as string
        System.out.println(player1.display());
        System.out.println(player2.display());
        
    }

    /**
     *  method to display welcome message before enter name
     *
     * @return             Some  as display.
     */
    public void gameWelcome()
    {
        System.out.println("welcome to play game ");
        System.out.println("==================== ");
        //
    }

    /**
     *  method to get player guess number, check in [1,100] and store
     *@param    low          An int to low range.
     *@param    high          An int to select high range.
     * @return     manguess      verified player guess number  as int.
     */
    public int humanGuess(int low,int high)
    {
        Scanner console = new Scanner(System.in);
        int manguess;
        String s;
        System.out.println("Enter guss number in [" +low+","+high+"]");
        //check if no numeric characters
        do
        { 
            try 
            {
                s = console.nextLine();
                manguess = Integer.parseInt(s);
                break;
            }
            catch (Exception e)//if no numeric warning
            {
                System.out.println("only Integer please try again");
            }
        }
        while (true);

        
        //loop check number not in [1,100] ask enter new
        while(manguess > 100 || manguess < 1)
        {
            if(manguess == 999)//number 999 means give up this round
            {
                break;
            }
            manguess = humanGuess(low,high);//ask new number
        }

        if (manguess > high || manguess < low)//check if out of range and warning
        {
            //warning message
            System.out.println("your number are not in range " +low + " to " +high);
        }
        System.out.println(" player guess number: " + manguess );
        return manguess;
    }

    /**
     *  method to check & store player enter name 
     *@param    mode          An int to select player1 is human or computer.
     * @return            player1 state  as display.
     */
    public void nameEnter(int mode)
    {
        Scanner console = new Scanner(System.in);
        System.out.println("user name");
        String uName = console.nextLine();
        String pcName = "PCgamer";

        if(mode == 1)
        {
            player1.setName(uName);
            player2.setName(pcName);
            System.out.println(player1.display());
        }
        else if(mode == 2)
        {
            player2.setName(uName);
            player1.setName(pcName);
            System.out.println(player2.display());
        }
        System.out.println(player1.getName()+" is first player and second player is: " + player2.getName());
    }

    /**
     *  method to generate hidden guess number
     *
     * @return     guessnum      generate hidden guess number  as int.
     */
    public int numberGuess()
    {
        int guessnum = numberGenerator.generateRandomNumber(100);
        return guessnum;
    }

    /**
     *  method to check which player get score  in one round
     *
     * @param attempt     attempt number as a int.
     * @param onegiveup    player1 give up flag as a boolean.
     * @param twpgiveup    player1 give up flag as a boolean.
     * @return              who is winner of this round as display.
     */
    public void playerScore(int attempt, boolean onegiveup, boolean twogiveup)
    {
        
        if(twogiveup == true)//player2 give up player1 win
        {
            player1.setScore(scoreGet(attempt));//check player1 score get and store
            System.out.println(player2.getName()+" give up this turn!" );//player2 giveup display
            System.out.println(player1.getName()+" get score this round: " + scoreGet(attempt) );//player1 get score display
        }
        else if(onegiveup == true)//player1 give up player2 win
        {
            player2.setScore(scoreGet(attempt));//check player2 score get and store
            System.out.println(player1.getName()+" give up this turn!" );//player1 giveup display
            System.out.println(player2.getName()+" get score this round: " + scoreGet(attempt) );//player2 get score display
        }
        else if(attempt % 2 == 1)//player1 turn and number correct
        {
            player1.setScore(scoreGet(attempt));//check player1 score get and store
            System.out.println(player1.getName()+" get score this round: " + scoreGet(attempt) );//player1 get score display
        }
        else if(attempt % 2 == 0)//player2 turn and number correct
        {
            player2.setScore(scoreGet(attempt));//check player2 score get and store
            System.out.println(player2.getName()+" get score this round: " + scoreGet(attempt) );//player2 get score display
        }
    }
    /**
     *  method to start one turn welcome
     *
     * @param round       round number as a int.
     * @return            welcome string  as display.
     */
    public void roundWelcome(int round)
    {
        System.out.println("Round "+round+" game start");
        System.out.println("===============");
    }
    
    /**
     *  method to check score get in one round
     *
     * @param attempt     attempt number as a int.
     * @return  score     score get in one round as int.
     */
    public int scoreGet(int attempt)
    {
        int score = 0;
        switch(attempt)
        {
            case 1:
                score = 18;
                break;
            case 2:
                score = 12;
                break;
            case 3:
                score = 8;
                break;
            case 4:
                score = 5;
                break;
            case 5:
                score = 3;
                break;
            case 6:
                score = 2;
                break;
        }
        return score;
    }




    /**
     * Method to start the program.
     *
     * @param args          An array of Strings representing command line arguments.
     */
    public static void main(String[] args)
    {
        Game objGame = new Game();
        objGame.gameWelcome();//display welcome message before start
        int mode = (int)(Math.random() * 2) + 1;//mode[1,2] 1 player first,2 computer first
        objGame.nameEnter(mode);//player enter name check & store
        int round = 1;
        while(round < 5)//this loop check game round <= 4
        {
            objGame.roundWelcome(round);//start one turn welcome
            objGame.gameStart(mode);//start one turn function
            round++;//move to next round
        }
        objGame.gameEnd();//check who is winner
    }

    /**
     * Mutator method to set the player1.
     *
     * @param   player1  player1 state.
     */
    public void setPlayer1(Player player1)
    {
        this.player1 = player1;
    }
	
	/**
     * Mutator method to set the player2.
     *
     * @param   player2  player2 state.
     */
    public void setPlayer2(Player player2)
    {
        this.player2 = player2;
    }

}
