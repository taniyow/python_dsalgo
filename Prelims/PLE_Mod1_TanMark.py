def collections():
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
    print("[11] Exit")
    def execute():
        try:
            num_list = []
            for i in range(10):
                numbers = int(input("Enter 10 numbers (enter each number): "))
                num_list.append(numbers)
            print("Original list: ", num_list)
        except:
            print("Invalid input. Your input will reset. Please try again")
            execute()
        ans = "Y"
        while ans=="Y":
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Menu 1")
                add_num = int(input("Enter a number to add: "))
                num_list.append(add_num)
                print("New lis after adding: ", num_list)
                ans = input("Try again?[Y/N]Answer: ")
            elif choice == "2":
                print("Menu 2")
                index = int(input("Enter the Index you want to insert value to: "))
                value = int(input("Enter the new value to insert: "))
                num_list.insert(index,value)
                print("New list after inserting: ", num_list)
                ans = input("Try again?[Y/N]Answer: ")

            elif choice == "3":
                print("Menu 3")
                delete = int(input("Enter the index of element you want to delete: "))
                num_list.pop(delete)
                print("New list after deleting: ", num_list)
                ans = input("Try again?[Y/N]Answer: ")

            elif choice == "4":
                print("Menu 4")
                total = sum(num_list)
                print("The sum of the elements: ", total)
                ans = input("Try again?[Y/N]Answer: ")
                
            elif choice == "5":
                print("Menu 5")
                ncount = int(input("Enter the number you want to count: "))
                num = num_list.count(ncount)
                print("The number of ", ncount, "in the list: ", num)
                ans = input("Try again?[Y/N]Answer: ")

            elif choice == "6":
                print("Menu 6")
                element = int(input("Enter the element you want to display: "))
                display = num_list.index(element)
                print(element, "is in index", display)
                ans = input("Try again?[Y/N]Answer: ")

            elif choice == "7":
                print("Menu 7")
                print("List contains: ", num_list)
                highest = max(num_list)
                lowest = min(num_list)
                print("The highest value is: ", highest)
                print("The lowest value is: ", lowest)
                ans = input("Try again?[Y/N]Answer: ")
                
            elif choice == "8":
                print("Menu 8")
                num_list.sort()
                print("Sorted List: ", num_list)
                ans = input("Try again?[Y/N]Answer: ")

            elif choice == "9":
                print("Menu 9")
                num_list.reverse()
                print("Reverse list: ", num_list)
                ans = input("Try again?[Y/N]Answer: ")

            elif choice == "10":
                print("Menu 10")
                element = int(input("Enter the element you want to remove: "))
                num_list.remove(element)
                print("New list after removing: ", num_list)
                ans = input("Try again?[Y/N]Answer: ")
                
            elif choice == "11":
                quit()

            else:
                print("Invalid input.")
                ans = input("Try again?[Y/N]Answer: ")
            
    execute()

collections() 
