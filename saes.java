import java.util.*;


public class saes
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int P10[] = { 3, 5, 2, 7, 4, 10, 1, 9, 8, 6 };
        int P8[] = { 6, 3, 7, 4, 8, 5, 10, 9 };
        int key1[] = new int[8];
        int key2[] = new int[8];
        int[] IP = { 2, 6, 3, 1, 4, 8, 5, 7 };
        int[] EP = { 4, 1, 2, 3, 2, 3, 4, 1 };
        int[] P4 = { 2, 4, 3, 1 };
        int[] IP_inv = { 4, 1, 3, 5, 7, 2, 8, 6 };
        System.out.println("Enter the Plaintext : ");
        int[] ptext=new int[8];
        int[] key=new int[8];
        for (int i=0;i<8;i++)
        {
            ptext[i]=sc.nextInt();
        }
        System.out.println("\nThe Plaintext message is : ");
        for (int i=0;i<8;i++)
        {
            System.out.print(ptext[i]+" ");
        }

        System.out.println("\nEnter the key of 8 bits : ");
        for (int i=0;i<8;i++)
        {
            key[i]=sc.nextInt();
        }
        System.out.println("\nThe key is : ");
        for (int i=0;i<8;i++)
        {
            System.out.print(key[i]+" ");
        }System.out.println("\n");

        int[][] S0 = { { 1, 0, 3, 2 },
                   { 3, 2, 1, 0 },
                   { 0, 2, 1, 3 },
                   { 3, 1, 3, 2 } };

        int[][] S1 = { { 0, 1, 2, 3 },
                   { 2, 0, 1, 3 },
                   { 3, 0, 1, 0 },
                   { 2, 1, 0, 3 } };

        void key_genr()
        {
            int n_key[]=new int[10];

        }
    }
};