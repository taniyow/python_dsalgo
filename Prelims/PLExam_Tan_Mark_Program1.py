def MAIN():
    print("--------------Main Menu-------------")
    print("[1]\tStack")
    print("[2]\tQueue")
    print("[3]\tExit")
    stack = []
    queue = []
    def Stack():
        def push():
            add = input("Enter value to add in stack: ")
            stack.append(add)
            print("Stack contains: ")
            size = len(stack)
            for i in range(size-1,-1,-1):
                print(stack[i])
            Stack()
               
        def pop():
            print("Pop value: ", stack.pop(-1))
            print("Stack Contains after pop(): ")
            size = len(stack)
            for i in range(size-1,-1,-1):
                print(stack[i])
            Stack()

        def stackMenu():
            try:
                print("\nStack Menu")
                print("[1]\tPush value\n[2]\tPop value\n[3]\tMain Menu\n")
                choice = int(input("Enter choice of number from Stack Menu: "))
                if choice == 1:
                    push()
                elif choice == 2:
                    pop()
                elif choice == 3:
                    MAIN()
            except:
                print("Invalid. Please try again.")
                stackMenu()
        stackMenu()

    def Queue(): #Queue Menu
        def enqueue():
            add = input("Enter the value to queue: ")
            queue.append(add)
            print("Queue contains: ")
            size = len(queue)
            for i in range(size):
                print(queue[i])
            Queue()
            
        def dequeue():
            print("Dequeue value: ", queue.pop())
            print("Queue Contains after dequeue: ")
            for i in range(len(queue)):
                print(queue[i])
            Queue()

        def queueMenu():
            try:
                print("\nQueue Menu")
                print("[1]\tEnqueue value\n[2]\tDequeue value\n[3]\tMain Menu\n")
                choice = int(input("Enter choice of number from Stack Menu: "))
                if choice == 1:
                    enqueue()
                elif choice == 2:
                    dequeue()
                elif choice == 3:
                    MAIN()
            except:
                print("Invalid. Please try again.")
                queueMenu()
        queueMenu()

    #MAIN MENU CHOICES
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            Stack()
        elif choice == 2:
            Queue()
        elif choice == 3:
            exit()
    except:
        print("Invalid input.")
        MAIN()
        
MAIN()
