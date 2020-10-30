# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

x = 100-age
y = 2020+x
print("You will turn 100 years old in {} years, in {}". format(x,y))
