import random
import string
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(text, shift):
    return caesar_cipher(text, -shift)

def main():
    os.system('clear')
    print('''\033[0;35m\t
     __   ___  __   __   ___ ___ 
    /__` |__  /  ` |__) |__   |  
    .__/ |___ \__, |  \ |___  |  
                               
                       by linux
                             
    \033[0m\n''')
    print("1. Encrypt message using Caesar cipher")
    print("2. Decrypt message using Caesar cipher")
    choice = input("Enter your choice:- ")


    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value for the Caesar cipher: "))
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value for the Caesar cipher: "))
        decrypted_message = decrypt_caesar(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


