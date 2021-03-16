# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Please put your name: ")
age = int(input("Please put your age: "))
year = 2021+(100-age)
print("{} will turn 100 years old in {}". format(name, year))
