import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

p = int(input("Enter the 1st Prime No. : "))
q = int(input("Enter the 2nd Prime No. : "))

if is_prime(p) and is_prime(q):
    n = p * q
    print("n =", n)

    if is_prime(n):
        phi_n = n - 1
    else:
        phi_n = (p - 1) * (q - 1)
    print("Phi(n) =", phi_n)


    e = int(input("Enter the value of e : "))
    if (gcd(e,phi_n)!=1):
        print("Error: gcd(e, Phi(n)) is not 1. Please choose another value for e.")
        exit()
        
    print("Calculating the value of d from the formula : d*e≡1(modϕ(n))")
    d = pow(e, -1, phi_n)
    print("d =", d)
    
    public_key = {'e': e, 'n': n}
    print("\nPublic key is : {", end="")
    for key, value in public_key.items():
        print(key, ":", value, end="")
        if key != 'n':
            print(",", end=" ")
        else:
            print("}")
            
    private_key = {'d': d, 'n': n}
    print("\nPrivate key is : {", end="")
    for key, value in private_key.items():
        print(key, ":", value, end="")
        if key != 'n':
            print(",", end=" ")
        else:
            print("}")

    M = int(input("Enter the value of Plain Text : "))

    # Encryption: C = M^e mod n
    print("\nPerforming Encryption of Plaintext M from the formula : C = M^e mod n\n")
    C = pow(M, e, n)
    print("Encrypted message (C) =", C)

    # Decryption: M = C^d mod n
    print("\nPerforming Decryption of Ciphertext C from the formula : M = C^d mod n\n")
    decrypted_message = pow(C, d, n)
    print("Decrypted message (M) =", decrypted_message)

else:
    print("One or both of the entered numbers are not prime.")

'''
Output:
PS D:\Ayush\College\Sem VI\Lab\IS\Code> python -u "d:\Ayush\College\Sem VI\Lab\IS\Code\Assignment_4\rsa.py"
Enter the 1st Prime No. : 3
Enter the 2nd Prime No. : 11
n = 33
Phi(n) = 20
Enter the value of e : 7
Calculating the value of d from the formula : d*e≡1(modϕ(n))
d = 3

Public key is : {e : 7, n : 33}

Private key is : {d : 3, n : 33}
Enter the value of Plain Text : 2

Performing Encryption of Plaintext M from the formula : C = M^e mod n

Encrypted message (C) = 29

Performing Decryption of Ciphertext C from the formula : M = C^d mod n

Decrypted message (M) = 2
PS D:\Ayush\College\Sem VI\Lab\IS\Code> 
'''