def seatPlan():
    seats = [['*','*','X','*','X','X'],
             ['*','X','*','X','*','X'],
             ['*','*','X','X','*','X'],
             ['X','*','X','*','X','X'],
             ['*','X','*','X','*','*'],
             ['*','X','*','*','*','X'],
             ['X','*','*','*','X','X'],
             ['*','X','*','X','X','*'],
             ['X','*','X','X','*','X'],
             ['*','X','*','X','X','X'],
             ['*','*','X','*','X','*'],
             ['*','*','X','X','*','X'],
             ['*','*','*','*','X','*']]
    ans ="Y"
    while ans == "Y":
        print("\tA\tB\tC\tD\tE\tF")
        for i in range(len(seats)):
            print("Row {}\t".format(i+1), end="")
            for j in range(len(seats[i])):
                print(seats[i][j],end="\t")
            print()#Print seats
        
        def execute():
            try:
                print("Reserve a seat.")
                row = int(input("Row: "))
                column = int(input("Column: "))
                if seats[row-1][column-1] == "X": # -1 index starts at 0
                    print("Seat is occupied. Try Again")
                    firstClass()
                else:
                    seats[row-1][column-1] = "X" #change * to X
                    print("\nSuccessfully reserved the seat. Thank you\n")
                    ans = input("Reserve another seat?[Y/N]: ").upper()
            except:
                print("Invalid input.")
                execute()
                
        def user():
            print("\nTicket Type :\n[1]\tFirst Class\n[2]\tBusiness Class\n[3]\tEconomy Class\n[4]\tExit")
            choice = input("Enter choice: ")
            if choice == "1": #First Class
                print("\nFirst Class\n","%5s%4c%4c%4c%4c%4c%4c"%("","A","B","C","D","E","F"))
                print("Row 1\t",'   '.join(seats[0][0:7]))
                print("Row 2\t",'   '.join(seats[1][0:7]))
                execute()
            elif choice == "2": #Business Class
                print("\nBusiness Class\n","%5s%4c%4c%4c%4c%4c%4c"%("","A","B","C","D","E","F"))
                print("Row 3\t",'   '.join(seats[2][0:7]))
                print("Row 4\t",'   '.join(seats[3][0:7]))
                print("Row 5\t",'   '.join(seats[4][0:7]))
                print("Row 6\t",'   '.join(seats[5][0:7]))
                print("Row 7\t",'   '.join(seats[6][0:7]))
                execute()
            elif choice == "3": #Economy Class
                print("\nEconomy Class\n","%5s%4c%4c%4c%4c%4c%4c"%("","A","B","C","D","E","F"))
                print("Row 8\t",'   '.join(seats[7][0:7]))
                print("Row 9\t",'   '.join(seats[8][0:7]))
                print("Row 10\t",'   '.join(seats[9][0:7]))
                print("Row 11\t",'   '.join(seats[10][0:7]))
                print("Row 12\t",'   '.join(seats[11][0:7]))
                print("Row 13\t",'   '.join(seats[12][0:7]))
                execute()
            elif choice == "4":
                exit()
            else:
                print("Invalid choice")
                user()
        user()
seatPlan()
