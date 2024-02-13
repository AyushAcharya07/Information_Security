import java.util.*;

public class saes
{
	public void RotNib(int[] w)
	{
		int size1=w.length/2;
		int[] w1=new int[size1];
		int[] w2=new int[size1];
		w1=Arrays.copyOfRange(w,0,size1);
		w2=Arrays.copyOfRange(w,size1,w.length);
		System.arraycopy(w1, 0, w, 0, w1.length); 
        System.arraycopy(w2, 0, w, w1.length, w2.length); 
        System.out.println("The key after applying Rotate Nibble is : ");
        for (int i:w)
        {
        	System.out.print(i);
        }
		
	}
	
	public void SubNib(int[] w)
	{
		
	}
	
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		int[] ptext=new int[16];
		int[] key=new int[16];
		int[] k0=new int[8];
		int[] k1=new int[8];
		int[] k2=new int[8];
		int[] k3=new int[8];
		int[][] Sbox={{1001,0100,1010,1011},
					  {1101,0001,1000,0101},
					  {0110,0010,0000,0011},
					  {1100,1110,1111,0111}}
					  
		int[][] Sbox_Search={{0000,0001,0010,0011},
					  {0100,0101,0110,0111},
					  {1000,1001,1010,1011},
					  {1100,1101,1110,1111}}
		
		System.out.println("Enter the 16-Bit Plaintext : ");
		for (int i=0;i<16;i++)
		{
			ptext[i]=sc.nextInt();
		}
		System.out.println("\nEnter the 16-Bit Key : ");
		for (int i=0;i<16;i++)
		{
			key[i]=sc.nextInt();
		}
		System.out.println("\nThe 16-Bit Plaintext message is : ");
		for (int i:ptext)
		{
			System.out.print(i);
		}
		System.out.println("\nThe 16-Bit Key is : ");
		for (int i:key)
		{
			System.out.print(key[i]);
		}
		System.out.println("\n");
		System.out.println("Now,generating the keys k0 and k1 from key!");
		int size=key.length/2;
		k0=Arrays.copyOfRange(key,0,size);
		k1=Arrays.copyOfRange(key,size,key.length);
		System.out.println("\nThe k0 key is : ");
		for (int i:k0)
		{
			System.out.print(i);
		}
		System.out.println("\n");
		System.out.println("\nThe k1 key is : ");
		for (int i:k1)
		{
			System.out.print(i);
		}
		System.out.println("\n");
		
	}
}
