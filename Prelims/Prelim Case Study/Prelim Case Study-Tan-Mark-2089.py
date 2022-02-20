#Tan, Mark Christian
#2089
#WD-201

def MAIN_MENU():
    print("\n\n----------------------------------------\nModular Program\n----------------------------------------")
    print("[1] \tPrelim Lab Exercise 1")
    print("[2] \tPrelim Lab Exercise 2")
    print("[3] \tPrelim Lab Exercise 3")
    print("[4] \tExit Program")
    
    def Module1():
        def execute1():
            def catch1():
                print("\nPLE 1 List Menu")
                print("[1] Append a number")
                print("[2] Insert a number in desired position")
                print("[3] Delete an index")
                print("[4] Sum the list")
                print("[5] Count the number of times a certain number is in the list")
                print("[6] Display an Index of the 1st position of number")
                print("[7] Display the highest and lowest value in the list")
                print("[8] Sort the elements in Ascending Order")
                print("[9] Reverse the order of the element")
                print("[10] Remove the element")
                print("[11] Main Menu")
                choice1 = input("Enter your choice: ")
                if choice1 == "1":
                    print("\nMenu 1")
                    add_num = int(input("Enter a number to add: "))
                    num_list.append(add_num)
                    print("New list after adding: ", num_list)
                    catch1()
                    
                elif choice1 == "2":
                    print("\nMenu 2")
                    index = int(input("Enter the Index you want to insert value to: "))
                    value = int(input("Enter the new value to insert: "))
                    num_list.insert(index,value)
                    print("New list after inserting: ", num_list)
                    catch1()

                elif choice1 == "3":
                    print("\nMenu 3")
                    delete = int(input("Enter the index of element you want to delete: "))
                    num_list.pop(delete)
                    print("New list after deleting: ", num_list)
                    catch1()

                elif choice1 == "4":
                    print("\nMenu 4")
                    total = sum(num_list)
                    print("The sum of the elements: ", total)
                    catch1()
                    
                elif choice1 == "5":
                    print("\nMenu 5")
                    ncount = int(input("Enter the number you want to count: "))
                    num = num_list.count(ncount)
                    print("The number of ", ncount, "in the list: ", num)
                    catch1()

                elif choice1 == "6":
                    print("\nMenu 6")
                    element = int(input("Enter the element you want to display: "))
                    display = num_list.index(element)
                    print(element, "is in index", display)
                    catch1()

                elif choice1 == "7":
                    print("\nMenu 7")
                    print("List contains: ", num_list)
                    highest = max(num_list)
                    lowest = min(num_list)
                    print("The highest value is: ", highest)
                    print("The lowest value is: ", lowest)
                    catch1()
                    
                elif choice1 == "8":
                    print("\nMenu 8")
                    num_list.sort()
                    print("Sorted List: ", num_list)
                    catch1()

                elif choice1 == "9":
                    print("\nMenu 9")
                    num_list.reverse()
                    print("Reverse list: ", num_list)
                    catch1()

                elif choice1 == "10":
                    print("\nMenu 10")
                    element = int(input("Enter the element you want to remove: "))
                    num_list.remove(element)
                    print("New list after removing: ", num_list)
                    catch1()
                    
                elif choice1 == "11":
                    MAIN_MENU()

                else:
                    print("Invalid input. Returning to PLE 1")
                    catch1()
            try:
                num_list = []
                for i in range(10):
                    numbers = int(input("Enter 10 numbers (enter each number): "))
                    num_list.append(numbers)
                print("Original list: ", num_list)
                catch1()
            except:
                print("Invalid input. Your input will reset. Please try again")
                catch1()
        execute1()

    def Module2():
        print("\nPLE 2 File Handling Menu")
        print("[1] Activity 1")
        print("[2] Activity 2")
        print("[3] Activity 3")
        print("[4] Main Menu")
        def act1():
            file = open('word.txt', 'r')
            #this splits the string in the file
            stringSplit = file.read().split() 

            unique_words = set(stringSplit)
            count_words = str(unique_words)
            for wrd in unique_words:
                print(wrd.strip('\'",.:;'), count_words.count(wrd))
            Module2()
        def act2():
            print("\nPLE 2 Activity 2 Menu")
            print("[1] Append data on File")
            print("[2] Read data on File")
            print("[3] Write data on File")
            print("[4] PLE 2 Menu")
            print("[5] Main Menu")
            choice21 = input("Enter your choice: ")
            def append():
                with open('names.txt','a') as file:
                    name = input("Enter name additional name in file: ")
                    file.write(name)
                    file.write('\n')
                act2()

            def read():
                with open('names.txt','r') as file:
                    print("The file contains the following: \n", file.read())
                act2()


            def write():
                with open('names.txt','w') as file:
                    name = input("Enter name in file: ")
                    file.write(name)
                    file.write('\n')
                act2()
            #module2 activity2 choices
            if choice21 == "1":
                append()
            elif choice21 == "2":
                read()
            elif choice21 == "3":
                write()
            elif choice21 == "4":
                Module2()
            elif choice21 == "5":
                MAIN_MENU
            else:
                print("Invalid input. Returning to PLE 2 Activity 2")
                act2()
        def act3():
            with open('sales.txt', 'r') as file:
                read = [float(i.strip ('\n')) for i in file.readlines()]
                print("List of Sales in Php")
                for n in range(len(read)):
                    print("Day {} : {}".format(n+1,read[n]))
                print("Total Sales Amount: Php {}".format(sum(read)))
                average = sum(read)/len(read)
                print("Average of Sales: Php {}".format(round(average,4)))
            Module2()
                
        #module2 choices
        choice2 = input("Enter your choice: ")
        if choice2 == "1":
            act1()
        elif choice2 == "2":
            act2()
        elif choice2 == "3":
            act3()
        elif choice2 == "4":
            MAIN_MENU()
        else:
            print("Invalid input. Returning to PLE 2")
            Module2()

    def Module3():
        print("\nPLE 3 Dictionary Menu")
        print("[1] Activity 1")
        print("[2] Activity 2")
        print("[3] Activity 3")
        print("[4] Main Menu")
        def activity1():
            expressway = { 'Tplex': 'Pangasinan' , 'Slex':'Subic' , 'Cavitex':'Bacoor,Cavite' , 'Mcx':'Muntinlupa' , 'Star Tollway':'Laguna' }
            for express, city in expressway.items():
                print("The "+ express + " runs through " + city + ".")

            print("\nThe following Expressway are included in this data set:")
            for express, city in expressway.items():
                print("- " + express)

            print("\nThe following Provinces are included in this data set:")
            for express, city in expressway.items():
                print("- " + city)
            Module3()
        def activity2():
            print("\nPLE 3 Activity 2 Menu")
            print("[1] Add a key pair value")
            print("[2] Check key in dictionary")
            print("[3] Remove a given key from dictionary")
            print("[4] Display values of dictionary")
            print("[5] PLE 3 Menu")
            print("[6] Main Menu")
            choice31 = input("Enter your choice: ")
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
                activity2()

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
                activity2()
            
            #Remove a key
            def removeKey():
                key = input("Enter key to remove: ")
                with open('dictionaryKo.txt', 'r') as file:
                    Dict = eval(file.read()) #convert the string from file to dict
                    del Dict[str(key)]
                with open('dictionaryKo.txt', 'w') as file: #rewrite the file with the updated dict
                    file.write(str(Dict))
                activity2()

            #Display values of dict
            def displayValues():
                with open('dictionaryKo.txt','r') as file:
                    read = eval(file.read())
                    for keys, values in read.items():
                        print(values)
                activity2()
            
            #module 3 activity 2 choices
            try:
                if choice31 == "1":
                    addKey()
                elif choice31 == "2":
                    checkKey()
                elif choice31 == "3":
                    removeKey()
                elif choice31 == "4":
                    displayValues()
                elif choice31 == "5":
                    Module3()
                elif choice31 == "6":
                    MAIN_MENU()
                else:
                    print("Invalid input. Returning to PLE 3 Activity 2")
                    activity2()
            except:
                print("Error Caught. Returning to Module 3 Activity 2 Menu")
                activity2()
                
        def activity3():
            file_name = input("Enter file name: ")
            search = input("Enter letter to be searched: ") 
            with open(file_name, 'r') as file:
                occur = 0
            
                for lines in file:
                    contents = lines.split()
                    for i in contents:
                        for letter in i:
                            if (letter == search):
                                occur+=1
                print("Occurrences of the letter:", occur)
            Module3()
        #module3 choices
        choice3 = input("Enter your choice: ")
        if choice3 == "1":
            activity1()
        elif choice3 == "2":
            activity2()
        elif choice3 == "3":
            activity3()
        elif choice3 == "4":
            MAIN_MENU()
        else:
            print("Invalid input. Returning to PLE 3")
            Module3()

    try:
    #main menu choices
    menu_choice = input("Enter main menu choice: ")
    if menu_choice == "1":
        Module1()
    elif menu_choice == "2":
        Module2()
    elif menu_choice == "3":
        Module3()
    elif menu_choice == "4":
        exit()
    except:
        print("Error Caught.---------------------------------------------")
        MAIN_MENU()
        
MAIN_MENU()
