import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class md5 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the message : ");
        String input = sc.nextLine();
        
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes()); 
            // input.getBytes() converts input into array of bytes and digest method computes hash values
            BigInteger number = new BigInteger(1, messageDigest);
            // creates BigInteger obj as number . 1-> means it has positive value and msgdigest is the byte array having hash value
            String md5 = number.toString(16);
            // toString(16) converts the BigInteger to a hexadecimal string representation.
            System.out.println("Input: " + input);
            System.out.println("MD5 Hash: " + md5);
        } catch (NoSuchAlgorithmException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
