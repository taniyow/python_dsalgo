#Tan,Mark Christian WD-201
def binaryTree():
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
        def printTree(self):
            if self.left:
                self.left.printTree()
            print(self.data, end='-'),
            if self.right:
                self.right.printTree()
        def insert(self, data):
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
                else:
                    self.data = data
                
    #traversals
    def PreOrder(root):
        if root:
            print(root.data, end='-')
            PreOrder(root.left)
            PreOrder(root.right)

    def InOrder(root):
        if root:
            InOrder(root.left)
            print(root.data, end='-')
            InOrder(root.right)

    def PostOrder(root):
        if root:
            PostOrder(root.left)
            PostOrder(root.right)
            print(root.data, end="-")

    print("Input menu")
    print("[1]\tInput numbers for Nodes")
    print("[2]\tInput letters for Nodes")
    inputchoice = int(input("Enter choice: "))
    if inputchoice==1:
        num = int(input("Enter number of elements: "))
        value = input("Enter Root node data: ") #root node data
        root = Node(value) #init var root node
        for i in range(num-1):
            add = input("Enter node data to insert: ")
            if add.isdigit():
                root.insert(add)
            else:
                print("Input is not Digit.\n\n")
                binaryTree()
        print("Binary Tree contains : ")
        root.printTree()
    elif inputchoice==2:
        num = int(input("Enter number of elements: "))
        value = input("Enter Root node data: ") #root node data
        root = Node(value) #init var root node
        for i in range(num-1):
            add = input("Enter node data to insert: ")
            if add.isdigit():
                print("Input is not Letters.\n\n")
                binaryTree()
            else:
                root.insert(add)
        print("Binary Tree contains : ")
        root.printTree()
    else:
        print("Invalid input.")

    def Menu():
        print("\n\nTraversal Menu")
        print("[A] Display Pre-Order traversal")
        print("[B] Display In-Order traversal")
        print("[C] Display Post-Order traversal")
        print("[D] Restart the Program")
        print("[E] Exit")
        choice = input("Enter choice: ").upper()
        return choice

    while True:
        choice = Menu()
        print()
        if choice == "A":
            print("Pre Order Traversal\n")
            PreOrder(root)
        elif choice == "B":
            print("In Order Traversal\n")
            InOrder(root)
        elif choice == "C":
            print("Post Order Traversal\n")
            PostOrder(root)
        elif choice == "D":
            print("Restarting program...\n\n")
            binaryTree()
        elif choice == "E":
            print("Exiting program...")
            exit()
        else:
            print("Invalid input. Please try again.")
            True
binaryTree()
        
