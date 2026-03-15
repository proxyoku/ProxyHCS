import hashlib

def crack_hash(hashFile, wordlistFile):
    try: 
        with open(hashFile,'r') as file:# open targetHash.txt in read only mode
            targetHash = file.read() #read file
    except FileNotFoundError: # built in python exception to check if file exists
        print("Error. Hash file not found.") # return error message if not found
        return

    try: 
        with open(wordlistFile,'r') as file:
            for line in file: # read each line in the wordlist
                word = line.strip() # using .strip to ignore leading or trailing characters
                # edit this line to change the hash type!
                hashed_word = hashlib.sha256(word.encode()).hexdigest() # convert current word to byte sequence, using utf 8 by default, then hash it

                if hashed_word == targetHash: # compare hash (of current word) to the target hash
                    print(f"Success! The password is: {word}")
                    return
        print("Password not found in the word list")
            
    except FileNotFoundError: 
        print("Error. wordlist file not found.") 
        return
    
crack_hash('targetHash.txt','wordlist.txt')

# both text files are closed automatically!