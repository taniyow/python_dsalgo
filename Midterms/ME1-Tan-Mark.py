def bubbleSort(array):
    loop1 = 1
    #run loops two times: one for walking through the array
    for i in range(len(array)):
        for j in range(0, len(array) - i -1):
            print("Loop ", loop1, " : ")
            #To sort in descending order, change > to < in this line.
            if array[j] > array[j+1]:
                
                #swap if greater is at the rear position
                (array[j], array[j+1]) = (array[j+1], array[j])
            print(array)
            loop1 = loop1 + 1
            
def selectionSort(array, size):
    loop1 = 1;
    for step in range(size):
        min_idx = step
        print("Loop ", loop1, " : ")
        for i in range(step + 1, size):
            #select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        #put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        loop1 = loop1+1
        print(array)
        
def mean(array):
    mean = sum(array)/len(array)
    print("Mean of Array: ", mean)

def median(data, size):
    if size % 2 == 0:
        median1 = data[len(data)//2] 
        median2 = data[len(data)//2 - 1] 
        median = (median1 + median2)/2
        print("Median of Array: ", median)
    else:
        median = data[len(data)//2]
        print("Median of Array: ", str(median))
        
def mode(array):
    from collections import Counter
    counter = Counter(array)
    getMode = dict(counter)
    mode = [k for k, v in getMode.items() if v == max(list(counter.values()))]
    get_mode = ', '.join(map(str, mode))
    print("Mode of array: " ,get_mode)

def negative(array):
    neg = []
    for i in array:
        if i < 0:
            neg.append(i)
    print("Negative value(s) array: ", neg)
    print("Sum of negative array is ", sum(neg))

def positive(array):
    pos = []
    for i in array:
        if i > 0:
            pos.append(i)
    print("Positive value(s) array: ", pos)
    print("Sum of positive array is ", sum(pos))

#main
data = []
num = int(input("Enter number of elements: "))
for i in range(num):
    add = int(input("Enter the element: "))
    data.append(add)
print("Array contains: ", data)
#menu
while True:
    print("Sort Menu\n[B] Bubble Sort\n[S] Selection Sort\n")
    choice = input("Enter Choice: ").upper()
    if choice == "B":
        bubbleSort(data)
        repeat = input("Do you want to try again?[Y/N]: ").upper()
        if repeat == "Y":
            True
        else:
            print("Sorted Array: ", data)
            print("Maximum value: ", max(data))
            print("Minimum value: ", min(data))
            mean(data)
            median(data, len(data))
            mode(data)
            negative(data)
            positive(data)
            print("End of the Program") 
            break
    elif choice == "S":
        size = len(data)
        selectionSort(data, size)
        repeat = input("Do you want to try again?[Y/N]: ").upper()
        if repeat == "Y":
            True
        else:
            print("Sorted Array: ", data)
            print("Maximum value: ", max(data))
            print("Minimum value: ", min(data))
            mean(data)
            median(data, len(data))
            mode(data)
            negative(data)
            positive(data)
            print("End of the Program") 
            break

#Tan,Mark Christian WD-201
