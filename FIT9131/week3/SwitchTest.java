public class SwitchTest
{
    public static void main(String[] args)
    {
        public static int random_int(int Min, int Max)
        {
            return (int) (Math.random()*(Max-Min))+Min;
        }




        int a = 1;
        switch(a)
        {
            default:
                System.out.println("Default");
                break;
            case 1:
                System.out.println("1");
            case 2:
                System.out.println("2");
                break;
        }
    }
}

