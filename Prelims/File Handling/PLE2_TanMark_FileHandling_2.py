def menu():

    #ask to go back to menu
    def tryAgain():
        answer = input("Try again?[Y/N] Answer: ")
        if answer == "Y" or answer == "y":
            return menu()
        else:
            print("Program Exit")
            exit()
    
    def append():
        file = open('names.txt','a')
        name = input("Enter name additional name in file: ")
        file.write(name)
        file.close()
        tryAgain()

    def read():
        file = open('names.txt','r')
        print("The file contains the following: \n", file.read())
        file.close()
        tryAgain()

    def write():
        file = open('names.txt','w')
        name = input("Enter name in file: ")
        file.write(name + '\n')
        file.close()
        tryAgain()

    #execute the program
    print("Menu")
    print("[A]\t Append data on the File \n[R]\t Read data on the File \n[W]\t Write data on the File \n[E]\t Exit")
    
    choice = input("Enter choice: ")
    if choice == "A" or choice == "a":
        append()
    elif choice == "R" or choice == "r":
        read()
    elif choice == "W" or choice == "w":
        write()
    elif choice == "E" or choice == "e":
        print("Program Exit")
        exit()
    else:
        print("Please try again. Input A R W E.")
        menu()
        
menu()
