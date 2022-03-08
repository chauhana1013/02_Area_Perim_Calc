from ast import Try
from multiprocessing.sharedctypes import Value
from urllib import response


# chesks  user has put a number more than zero
valid = False
while not valid:

    error = "Please enter a number more than zero"
    
    try:
            
        # ask user for a number
        response = float(input("Enter a number: "))
        
        # checks number is more than 0
        if response > 0:
            valid = True

        #outputs error if input is invalid 
        else:
            print(error)
            print()
    
    except ValueError: 
        print(error)