import java.util.Scanner;
public class Vowl
{
   public static void main(String args[])
   {
      
      int n;
      Scanner sc=new Scanner(System.in);
      System.out.println("enter the int:");
      n=sc.nextInt();
      
        {
         if(n==97 || n==101 || n==105 || n==111 || n==117)
           {
             System.out.println("letter is contain vowl.");
           }
         else
            {
              System.out.println("letter is not contain vowl.");
            }
        }
      
   }
}
