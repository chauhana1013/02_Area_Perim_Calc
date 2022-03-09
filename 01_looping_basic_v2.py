# functions go here

# checks number is more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number more than zero"
        
        try:
                
            # ask user for a number
            response = float(input(question))
            
            # checks number is more than 0
            if response > 0:
                return response

            #outputs error if input is invalid 
            else:
                print(error)
                print()
        
        except ValueError: 
            print(error)



# Main Routine goes here
print()
print("Hi, my name is Peri de Meterous or Peri for short")
print("Please enter the following...")

# Loop the whole code
go_again = ""
while go_again == "": 
    
    print()
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate Perimeter
    perimeter = 2 * (height + width)

    # Calculate Area
    area = width * height
 # Outputs rounded to 2 decimal places   
    print()
    print("The Perimeter is {:.2f}".format(perimeter))
    print("The Area is {:.2f}".format(area))
    print("Have a nice day")
    print()

    go_again = input("Press <enter> to calculate again or any key to stop")

print()
print("Glad to help you, see you next time")
