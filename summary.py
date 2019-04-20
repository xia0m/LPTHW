# define a variable
number_1 = 39
print(f"the number is {number_1}")

# user input
number_2 = input("Enter a number ")
print(f"the number entered is {number_2}")

# argument 

from sys import argv

#script, second = argv

# print(f"{script}, {second}")

# file input

script, filename = argv
txt = open(filename)
print(txt.read())

# write file
