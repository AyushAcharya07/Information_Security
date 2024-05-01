import math
import random

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

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def char_to_num(char):
    if char == ' ':
        return 0
    return ord(char.lower()) - ord('a')+1

def num_to_char(num):
    if num==0:
        return ' '
    return chr((num-1)%26+ord('a'))

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

    e = random.randint(2,phi_n-1)
    while gcd(e,phi_n)!=1:
        e = random.randint(2,phi_n-1)
        
    print("Generated value of e is : ",e)
    print("Calculating the value of d")
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
            
    message=input("Enter the plaintext message : ")
    
    #Encyption
    encrypted_message = []
    for char in message:
        num = char_to_num(char)
        encrypted_num = pow(num, e, n)
        encrypted_message.append(encrypted_num)
            
    encrypted_characters = [num_to_char(num) for num in encrypted_message]
    print("Encrypted message (characters) : ", ''.join(encrypted_characters))
    
    
    #Decryption
    decrypted_message=""
    for encrypted_num in encrypted_message:
        if encrypted_num == 0:  # Check for space character
            decrypted_char = " "
        else:
            decrypted_num = pow(encrypted_num, d, n)
            decrypted_char = num_to_char(decrypted_num)
        decrypted_message += decrypted_char

        
    print("Decrypted message : ",decrypted_message)

else:
    print("One or both of the entered numbers are not prime.")
