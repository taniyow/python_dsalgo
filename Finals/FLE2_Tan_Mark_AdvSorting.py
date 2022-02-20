def ShellSort(array, n):
    loop1 = 1
    for i in range(len(array)):
        print("Loop ", loop1)
        interval = n // 2
        while interval > 0:
            print(array)
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j-interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                array[j] = temp
            interval //=2
        loop1 +=1
        
def QuickSort(array):
    if len(array) <=1:
        return array
    else:
        pivot=array.pop()

    greater_items = []
    less_items = []

    for item in array:
        if item > pivot:
            greater_items.append(item)
        else:
            less_items.append(item)
    return QuickSort(less_items)+[pivot]+QuickSort(greater_items)

def InsertionSort(array):
    loop = 1
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1
            array[j+1] = key

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

def BubbleSort(array):
    loop = 1
    for i in range(len(array)):
        for j in range(0, len(array) - i -1):
            print("Loop ", loop, ":")
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
            print(array)
            loop = loop + 1

def SelectionSort(array, size):
    loop = 1
    for step in range(size):
        min_id = step
        print("Loop ", loop, ":")
        for i in range(step + 1, size):
            if array[i] < array[min_id]:
                min_id = i
        (array[step], array[min_id]) = (array[min_id], array[step])
        loop = loop + 1
        print(array)

def menu():
    print("\nSort Menu")
    print("[A]\tBubble Sort")
    print("[B]\tInsertion Sort")
    print("[C]\tMerge Sort")
    print("[D]\tQuick Sort")
    print("[E]\tSelection Sort")
    print("[F]\tShell Sort")
    print("[Q]\tQuit Program")
    choice = input("Enter Choice: ").upper()
    return choice

#execute

arr = []
num = int(input("Enter number of elements: "))
for i in range(num):
    element = int(input("Enter the element: "))
    arr.append(element)
print("Array contains: ", arr)
import copy
while True:
    choice = menu()
    if choice == 'A':
        arr_copy = arr.copy()
        print("\n******** Bubble Sort ********")
        print("Unsorted Array : ", arr_copy)
        BubbleSort(arr_copy)
        print("Sorted Array: ", arr_copy)
        
    elif choice == 'B':
        arr_copy = arr.copy()
        print("\n******** Insertion Sort ********")
        print("Unsorted Array : ", arr_copy)
        InsertionSort(arr_copy)
        print("Sorted Array: ")
        for i in range(len(arr_copy)):
            print(arr_copy[i], end= ' * ')
        
    elif choice == 'C':
        arr_copy = arr.copy()
        print("\n******** Merge Sort ********")
        print("Unsorted Array : ", arr_copy)
        MergeSort(arr_copy)
        print("Sorted Array: ")
        for i in range(len(arr_copy)):
            print(arr_copy[i], end= ' # ')
        
    elif choice == 'D':
        arr_copy = arr.copy()
        print("\n******** Quick Sort ********")
        print("Unsorted Array : ", arr_copy)
        print("Sorted Array: ", QuickSort(arr_copy))

    elif choice == 'E':
        arr_copy = arr.copy()
        print("\n******** Selection Sort ********")
        print("Unsorted Array : ", arr_copy)
        size = len(arr_copy)
        SelectionSort(arr_copy, size)
        print("Sorted Array: ", arr_copy)

    elif choice == 'F':
        arr_copy = arr.copy()
        print("\n******** Shell Sort ********")
        print("Unsorted Array : ", arr_copy)
        size = len(arr_copy)
        ShellSort(arr_copy, size)
        print("Sorted Array: ", arr_copy)
    
    elif choice == 'Q':
        print("\nEnd of Program")
        exit()
        
    else:
        print("\nInvalid Choice. Return to Sort Menu")

#Tan, Mark Christian M.
#WD - 201
