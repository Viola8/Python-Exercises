# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# Divisor is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

x = int(input("Please enter a number to identify its divisors: "))

for i in range(1,x+1):
    if x%i==0:
        print(i)

# for a list of devisors
x = int(input("Please enter a number to identify its divisors: "))

list_range = list(range(1,x+1))
list_of_devisors = []

for i in list_range:
    if x%i==0:
        list_of_devisors.append(i)

print(list_of_devisors)
