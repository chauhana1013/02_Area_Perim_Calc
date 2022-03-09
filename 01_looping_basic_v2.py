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
width = num_check("Width: ")
height = num_check("Height: ")

# Calculate Perimeter
perimeter = (width * 2) + (height * 2)

# Calculate Area
area = width * height

print()
print("The Perimeter is {} units and the Area is {} squared units".format(perimeter, area))
print()