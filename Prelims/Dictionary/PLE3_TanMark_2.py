print("Menu")
print("[A]\t Add a key pair value to a dictionary \n[B]\t Check if a given key exists in the dictionary or not \n[C]\t Remove a given key from the dictionary \n[D]\t Display the values of the dictionary \n[E]\t Exit")

def menu():
    
    #ask to go back to menu
    def tryAgain():
        answer = input("Try again?[Y/N] Answer: ")
        if answer == "Y" or answer == "y":
            return menu()
        else:
            print("Program Exit")
            exit()

    #add a key pair value to a dict
    def addKey():
        key = input("Enter key: ")
        value = input("Enter value: ")
        file = open('dictionaryKo.txt', 'a')
        with open('dictionaryKo.txt','r') as file:
            file.seek(0)
            first_char = file.read(1)
            if not first_char: #adds a dict in file if its empty
                with open('dictionaryKo.txt','w') as file:
                    dictionary = {key:value}
                    strDictionary = str(dictionary)
                    file.write(strDictionary)
            else: #read the file and write on it with the new updated dict
                file.seek(0)
                string = eval(str(file.read()))
                string.update({key:value})
                with open('dictionaryKo.txt','w') as file:
                    strDictionary = str(string)
                    file.write(strDictionary)
        tryAgain()

    #Check a key
    def checkKey():
        key = input("Enter key to check: ")
        with open('dictionaryKo.txt', 'r') as file:
            file.seek(0)
            first_char = file.read(1)
            if not first_char: #check file if its empty
                print("File is empty.")
            else:
                file.seek(0)
                Dict = eval(str(file.read()))
                if str(key) in Dict: #check key if it exists
                    print("The key ", key , " is in the dictionary.")
                else:
                    print("Key was not found.")
        tryAgain()
    
    #Remove a key
    def removeKey():
        key = input("Enter key to remove: ")
        with open('dictionaryKo.txt', 'r') as file:
            Dict = eval(file.read()) #convert the string from file to dict
            del Dict[str(key)]
        with open('dictionaryKo.txt', 'w') as file: #rewrite the file with the updated dict
            file.write(str(Dict))
        tryAgain()

    #Display values of dict
    def displayValues():
        with open('dictionaryKo.txt','r') as file:
            read = eval(file.read())
            for keys, values in read.items():
                print(values)
        tryAgain()
        

    #execute the program
    choice = input("Enter choice: ")
    if choice == "A" or choice == "a":
        addKey()
    elif choice == "B" or choice == "b":
        checkKey()
    elif choice == "C" or choice == "c":
        removeKey()
    elif choice == "D" or choice == "d":
        displayValues()
    elif choice == "E" or choice == "e":
        print("Program Exit")
        exit()
    else:
        print("Please try again. Inputs should only be [A/B/C/D/E].")
        menu()
        
menu()
