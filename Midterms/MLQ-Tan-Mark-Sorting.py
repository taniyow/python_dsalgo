#Tan,Mark Christian WD-201

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
    
#main
data = []
num = int(input("Enter number of elements: "))
for i in range(num):
    add = int(input("Enter the element: "))
    data.append(add)
print("Array contains: ", data)
if (num % 2) == 0:
    size = len(data)
    selectionSort(data, size)
    print("Selection Sorted Array in Ascending Order: ")
    print(data)
    median1 = data[len(data)//2] 
    median2 = data[len(data)//2 - 1] 
    median = (median1 + median2)/2
    print("\nMedian value of numbers: ", median)
    print("Minimum value of numbers: ", min(data))
    print("Maximum value of numbers: ", max(data))
else:
    bubbleSort(data)
    print("Bubble Sorted Array in Ascending Order: ")
    print(data)
    median = data[len(data)//2] 
    print("\nMedian value of numbers: ", median)
    print("Minimum value of numbers: ", min(data))
    print("Maximum value of numbers: ", max(data))

