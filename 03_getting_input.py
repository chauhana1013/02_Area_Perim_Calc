# Ask the user for their name
from tokenize import Double
username = input("What's ye name, mate?")

# Ask the user for thier favourite integer
fav_num = int(input("Favourite Number?"))

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num 

print()
# Greet the user 
print("{} I have guessed your favourite number and it is {}. I am a genius.".format(username, fav_num))
print()
# Output the results of doubling, halving 
# and squaring their favourite number
print("I doubled {} and it is {}".format(fav_num, double))
print("I halfed {}, halfing it will be {}".format(fav_num, half))
print("Also sqaring it will be {} and by the way, I am so smart".format(squared))