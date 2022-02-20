def sales():
    file = open('sales.txt', 'r')
    read = [float(i.strip ('\n')) for i in file.readlines()]
    print("List of Sales in Php")
    for n in range(len(read)):
        print("Day {} : {}".format(n+1,read[n]))
    print("Total Sales Amount: Php {}".format(sum(read)))
    average = sum(read)/len(read)
    print("Average of Sales: Php {}".format(round(average,4)))
    file.close
    
sales()
