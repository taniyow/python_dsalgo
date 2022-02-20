def word():
    ans = "Y"
    while ans == "Y" or ans == "y":
        file = open('word.txt', 'r')
        #this splits the string in the file
        stringSplit = file.read().split() 

        unique_words = set(stringSplit)
        count_words = str(unique_words)
        for wrd in unique_words:
            print(wrd.strip('\'",.:;'), count_words.count(wrd))
        ans = input("Try again?[Y/N]Answer: ")
    else:
        exit
word()
