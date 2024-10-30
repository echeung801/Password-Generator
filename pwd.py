import secrets

# This is a program made to help generate passwords for different job portal accounts


QUIT = False;

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
SYMBOLS = ["!","@","#","$","%","?","*"]
string = [] # initializing string



while not QUIT:
        length = int(input("Choose how long you want your new password to be. \n")) # user prompt

        for i in range(length): # for loop

                add = "" # the upper or lowercase letter / symbol being concatenated                
                whichArray = secrets.choice([0, 1, 2, 3])
                
                match whichArray: # switch case
                        case 0: # letter case lowercase
                                string.append(secrets.choice(ALPHABET))
                        
                        case 1: # letter case uppercase
                                string.append((secrets.choice(ALPHABET)).upper())
                                
                        case 2: # alphanumeric case
                                string.append(secrets.choice(SYMBOLS))
                        
                        case 3: # number case
                                string.append(secrets.choice(NUMBERS))
                        
        done = ''.join(string)

        print("Here is your new password: ", done, "\n")
        q = input("Would you like to generate another password? Enter 'q' to exit. Press any other key to continue. \n")
      
        if(q.lower() == 'q'):
                QUIT = True

        # else:
        string = []
        
print("bye!!!  :)")
