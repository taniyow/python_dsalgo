def expressways():
    expressway = { 'Tplex': 'Pangasinan' , 'Slex':'Subic' , 'Cavitex':'Bacoor,Cavite' , 'Mcx':'Muntinlupa' , 'Star Tollway':'Laguna' }
    for express, city in expressway.items():
        print("The "+ express + " runs through " + city + ".")

    print("\nThe following Expressway are included in this data set:")
    for express, city in expressway.items():
        print("- " + express)

    print("\nThe following Provinces are included in this data set:")
    for express, city in expressway.items():
        print("- " + city)

expressways()
