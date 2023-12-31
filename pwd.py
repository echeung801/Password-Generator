import random

# This is a program made by Ethan C. to help generate passwords for different job portal accounts


QUIT = False;

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
SYMBOLS = ["!","@","#","$","%","&","?"]
string = "" # initializing string



while not QUIT:
        length = int(input("Choose how long you want your new password to be. ")) # user prompt

        for i in range(0, length): # for loop

                add = "" # the upper or lowercase letter / symbol being concatenated                
                whichArray = int((random.random() * (1000 + random.random())) % 4) # random case chosen
                
                match whichArray: # switch case
                        case 0: # letter case lowercase
                                add = ALPHABET[int((random.random() * 1000 + random.random()%2 + random.random())) % 26]
                        
                        case 1: # letter case uppercase
                                add = (ALPHABET[int((random.random() * random.random() * 1000 + random.random()%3 + random.random())) % 26]).upper()
                                
                        case 2: # alphanumeric case
                                add = SYMBOLS[int((random.random() * random.random() * 1000 + random.random()%4 + random.random())) % 7]
                        
                        case 3: # number case
                                add = NUMBERS[int((random.random() * 1000 + random.random()%3 + random.random())) % 10]
                        
                string = string + add #concatenate string

    
        print("Here is your new password: ", string, "\n")
        q = input("Would you like to generate another password? Enter 'q' to exit. \n")
      
        if(q == "q"):
                QUIT = True

        # else:
        string = ""
        
print("bye!!!  :)")
