class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        printvalue = self.head
        while(printvalue):
            print(printvalue.data)
            printvalue = printvalue.next
            
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev

while True:
    llist = LinkedList()
    count = int(input("Enter the number of elements for Linked List : "))
    for i in range(count):
        data = int(input("Enter data in Linked list: "))
        llist.insert(data)

    print("The Linked List Original Order: ")    
    llist.printLinkedList()
    llist.reverse()
    print("The Linked List in Reverse Order: ")
    llist.printLinkedList()
    
    ans = input("Do you want to try again?[Y/N]:").upper()
    if ans == "Y":
        True
    else:
        print("Exiting program...")
        exit()

#TAN MARK CHRISTIAN
#WD 201
