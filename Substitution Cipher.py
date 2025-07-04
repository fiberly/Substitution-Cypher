import random
import string
import os

#Subs Cipher Part
class SubstitutionCipher:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.key = ''.join(random.sample(self.alphabet, len(self.alphabet)))

  # define encryption and decryption
    def encrypt(self, plaintext):
        # Encrypt plaintext using the substitution cipher key
        plaintext = plaintext.lower()
        return ''.join(self.alphabet[self.key.index(char)] if char in self.alphabet else char for char in plaintext)

  
    def decrypt(self, ciphertext):
        # Decrypt ciphertext back to plaintext using the substitution cipher key
        return ''.join(self.alphabet[self.key.index(char)] if char in self.key else char for char in ciphertext)

#User input Cipher and display
def handle_encrypt_decrypt(cipher):
        print("\nEncrypt/Decrypt Data: ")
        print("1. User Input")
        print("2. File Content")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            data  = input("Enter the text to encrypt: ")
        elif choice == '2':
            filename = input("Enter the filename: ")
            if not os.path.isfile(filename):
                print(f"File '{filename} not found.")
                return
            with open(filename, 'r') as file:
                data = file.read()
        else:
            print("Invalid Choice")
            return
        
    #Output
        print("\nOriginal Plaintext:")
        print(data)

        encrypted = cipher.encrypt(data)
        print("\nEncrypted Text:")
        print(encrypted)

        decrypted = cipher.decrypt(encrypted)
        print("\nDecrypted Text:")
        print(decrypted)



# Password Generator Part
    #def generated password
    # Generate a strong password based on user-defined criteria

    # Define the character pool based on user options

    # Generate a random password and ensure the password meets the criteria



#Main Menu and functionality
def main_menu():

    # Display the main menu and handle user choices
    cipher = SubstitutionCipher()

    while True:
        print("\nMain Menu:")
        print("1. Encrypt/Decrypt Data (User Input or File)")
        print("2. Generate a Password")
        print("3. Exit")
        choice = input("Enter your choice 1, 2, or 3: ")

        if choice == '1': 
            handle_encrypt_decrypt(cipher)
            
        elif choice =='3':
            print("Have a good time!")
            break
        else:
            print("Please pick only 1, 2, or 3")

    




#Run the program Dont touch
if __name__ == "__main__":
    main_menu()