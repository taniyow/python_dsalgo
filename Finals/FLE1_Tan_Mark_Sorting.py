def BubbleSort(array):
    loop = 1
    for i in range(len(array)):
        for j in range(0, len(array) - i -1):
            print("Loop ", loop, ":")
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
            print(*array, sep = ' ')
            loop += 1

def InsertionSort(array):
    loop = 1
    for i in range(1, len(array)):
        key = array[i]
        print("Loop ", loop, ":")
        while i>0 and array[i-1] > key:
            array[i] = array[i-1]
            i = i-1
            array[i] = key
            print(*array, sep = ' ')
        print(*array, sep = ' ')
        loop += 1

def MergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            array[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            array[k] = R[j]
            j+=1
            k+=1

def SelectionSort(array, size):
    loop = 1
    for step in range(size):
        min_id = step
        print("Loop ", loop, ":")
        for i in range(step + 1, size):
            if array[i] < array[min_id]:
                min_id = i
            (array[step], array[min_id]) = (array[min_id], array[step])
            loop += 1
            print(*array, sep = ' ')

#menu
def menu():
    print("\nSort Menu")
    print("[B] Bubble sort\n[I] Insertion Sort\n[M] Merge Sort\n[S] Selection Sort\n[E] Exit")
    choice = input("Enter Choice: ").upper()
    return choice

#execute
import copy
arr = []
num = int(input("Enter number of elements: "))
for i in range(num):
    element = int(input("Enter the element: "))
    arr.append(element)
print("Array contains: ", arr)

while True:
    choice = menu()
    if choice == "B":
        arr_copy = arr.copy()
        print("\nOriginal Array contains: ", arr_copy)
        print("******** Bubble Sort ********")
        BubbleSort(arr_copy)
        print("Sorted Array: ", *arr_copy, sep = ' ')
        
    elif choice == "I":
        arr_copy = arr.copy()
        print("\nOriginal Array contains: ", arr_copy)
        print("******** Insertion Sort ********")
        InsertionSort(arr_copy)
        print("Sorted Array: ", *arr_copy, sep = ' ')
        
    elif choice == "M":
        arr_copy = arr.copy()
        print("\nOriginal Array contains: ", arr_copy)
        print("******** Merge Sort ********")
        MergeSort(arr_copy)
        print("Sorted Array: ", *arr_copy, sep = ' ')
        
    elif choice == "S":
        arr_copy = arr.copy()
        print("\nOriginal Array contains: ", arr_copy)
        print("******** Selection Sort ********")
        size = len(arr_copy)
        SelectionSort(arr_copy, size)
        print("Sorted Array: ", *arr_copy, sep = ' ')

    elif choice == "E":
        print("Exiting Program...")
        exit()
    else:
        print("\nInvalid Choice. Return to Sort Menu")

#Tan, Mark Christian M.
#WD - 201
