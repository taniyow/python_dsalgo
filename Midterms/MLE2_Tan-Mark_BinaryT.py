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
        def search(self, key):
            if key < self.data:
                if self.left is None:
                    return str(key),' Not Found'
                return self.left.search(key)
            elif key > self.data:
                if self.right is None:
                    return str(key),' Not Found'
                return self.right.search(key)
            else:
                print(str(self.data), ' is found')
                
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

    #insertion of node data
    value = input("Enter Root node data: ") #root node data
    root = Node(value) #init var root node
    ans="Y"
    while ans=="Y":
        add = input("Enter node data to insert: ")
        root.insert(add)
        ans = input("Do you want to enter another data?[Y/N]: ").upper()
        
    print("Binary Tree contains : ")
    root.printTree()

    def Menu():
        print("\n\nBinary Tree Main Menu\n-----------------------")
        print("[1] Search a node")
        print("[2] Display Pre-Order traversal")
        print("[3] Display In-Order traversal")
        print("[4] Display Post-Order traversal")
        print("[5] Restart the Program")
        print("[6] Exit")
        choice = int(input("Enter choice: "))
        return choice

    while True:
        choice = Menu()
        print()
        if choice == 1:
            value = input("Enter data to search: ")
            print(root.search(value))
        elif choice == 2:
            print("Pre Order Traversal\n")
            PreOrder(root)
        elif choice == 3:
            print("In Order Traversal\n")
            InOrder(root)
        elif choice == 4:
            print("Post Order Traversal\n")
            PostOrder(root)
        elif choice == 5:
            print("Restarting program...\n\n")
            binaryTree()
        elif choice == 6:
            exit()
        else:
            print("Invalid input. Please try again.")
            True
binaryTree()
        
