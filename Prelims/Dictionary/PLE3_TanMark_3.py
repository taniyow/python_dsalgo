def occurences():
    ans = "Y"
    while ans == "Y":
        file_name = input("Enter file name: ")
        search = input("Enter letter to be searched: ") 
        with open(file_name, 'r') as file:
            occur = 0
        
            for lines in file:
                contents = lines.split()
                for i in contents:
                    for letter in i:
                        if (letter == search):
                            occur+=1
            print("Occurrences of the letter:", occur)
            ans = input("Try again?[Y/N]Answer: ")
    else:
        exit
occurences()
