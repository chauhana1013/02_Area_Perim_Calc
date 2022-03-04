valid = False
while not valid:

    try:
            
    #Ask user for n
    response = float(input("Enter a number: "))
    
    if response > 0:
        valid = True

    else:
        print("Please enter a number that is more than zero")
        print()