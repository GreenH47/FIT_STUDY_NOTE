/*
编写一个程序，通过键盘接受用户的两个输入： 单个字符（可以是字母、数字或符号） 
一个数字，代表一个必须在 5 到 10 之间（含 5 到 10）的级别。 
根据以上选择，系统会生成一个图案显示在屏幕上，如下图所示：
*/

import java.util.Scanner;

public class Pattern
{
    public static void printSquare(char icon,int n)
    {

        //up left
        for (int i = 0; i < n; i++) 
        {
            System.out.println();
            for (int j = 0; j <= i; j++) 
            {
                System.out.print(icon);
            }
        }

        //down left
        for (int i = n - 1; i > 0; i--)
        {
            System.out.println();
            for (int j = 0; j < i; j++) 
            {
                System.out.print(icon);
            }
        }
    }


    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);
        System.out.println("Enter print : ");
        String character = console.nextLine();
        char symbol = character.charAt(0);

        System.out.println("level? ");
        int level = console.nextInt();

        printSquare(symbol,level);
    }
}
