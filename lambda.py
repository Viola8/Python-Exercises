# Create a lambda function that adds 15 to a given number passed in as an argument
f = lambda y: y + 15
print(f(10))  # 25

# Create a lambda function that multiplies argument x with argument y and print the result.
f = lambda x,y: x*y
print(f(2,6))  # 12

# Write a Python program to square and cube every number in a given list of integers using Lambda.
list1 = [1,2,3,4,5,6]
print(list(map(lambda x: x*x, list1)))
print(list(map(lambda x: x**3, list1)))

# Write a Python program to filter a list of integers using Lambda.
list2 = [32,56,5,10,37,8]
print(list(filter(lambda y: y%2 == 0, list2))) # [32,56,10,8]
print(list(filter(lambda y: y%2 != 0, list2))) # [5,37]

# Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with("Python")) # True
print(starts_with("SQL")) # False
