# Write a Python program to get the last part of a string before a specified character.

# from https://www.w3resource.com/python-exercises to get https://www.w3resource.com/python without -exercises

str1 = "https://www.w3resource.com/python-exercises"

print(str1.rsplit('-', 1))

# OUTPUT: ['https://www.w3resource.com/python','exercises']

print(str1.rsplit('-', 1)[0])

# OUTPUT: 'https://www.w3resource.com/python'

print(str1.rsplit('-', 1)[1])

# OUTPUT: exercises
