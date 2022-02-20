class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        printListElements = self.head
        while printListElements:
            print(printListElements.data)
            printListElements = printListElements.next

    def search(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return current
            current = current.next
        return None
    
    def insertAtBeginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insertBetween(self, prev, value):
        if prev is None:
            self.head = new_node
            return
        node = Node(value)
        node.next = prev.next
        prev.next = node
    
    def insertAtEnd(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def delete(self, value):
        tmp = self.head
        if tmp is not None:
            if tmp.data == value:
                self.head = tmp.next
                tmp = None
                return
        while tmp is not None:
            if tmp.data == value:
                break
            prev = tmp
            tmp = tmp.next
        if tmp is None:
            print("Cannot delete node. Node does not exist.")
            return
        prev.next = tmp.next
        tmp = None

def Menu():
    print("\nLinked List\n--------------")
    print("[A] Insert new node value at Beginning")
    print("[B] Insert new node value Between 2 Nodes")
    print("[C] Insert new node value at End")
    print("[D] Delete Node")
    print("[E] Exit")
    choice = input("Enter choice: ").upper();
    return choice

linkedlist = LinkedList() #create variable for linkedlist   
while True:
    choice = Menu()
    print()
    if choice == "A":
        value = input("Enter value to insert at the beginning: ")
        linkedlist.insertAtBeginning(value)
        print("Linked List contains the following:")
        linkedlist.printLinkedList()
    elif choice == "B":
        prev = input("Enter the node you want to insert your new node value after: ")
        value = input("Enter value to insert: ")
        linkedlist.insertBetween(linkedlist.search(prev), value)
        print("Linked List contains the following:")
        linkedlist.printLinkedList()
    elif choice == "C":
        value = input("Enter value you want to insert at the end: ")
        linkedlist.insertAtEnd(value)
        print("Linked List contains the following:")
        linkedlist.printLinkedList()
    elif choice == "D":
        value = input("Enter value you want to delete: ")
        linkedlist.delete(value)
        print("Linked List contains the following:")
        linkedlist.printLinkedList()
    elif choice == "E":
        exit()
    else:
        print("Invalid input. Please try again.")
        True
