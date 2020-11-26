# Write a Python program to check whether a given string is number or not using Lambda.
is_number = lambda x: True if x.isdigit() else False
print(is_number("Python")) # False
print(is_number("4")) # True
# same for negative number and float
is_num = lambda y: y.replace('.','').isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
is_num1 = lambda z: is_num(z[1:]) if z[0]=='-' else is_num(z)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))

# Write a Python program to find intersection of two given arrays using Lambda.
list1 = [2,4,6,8,10]
list2 = [2,4,5,8,11]

intersection = list(filter(lambda x: x in list1, list2))
print(intersection)  # [2,4,8]

# Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
arr1 = [2,3,4,5,6,7,8]

print(len(list(filter(lambda x: x%2 == 0, arr1)))) # Output: 4 for odd numbers
print(len(list(filter(lambda x: x%2 != 0, arr1)))) # Output: 3 for even numbers
