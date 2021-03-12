# Write a Python program to convert the given list to string.
# 1 using for loop
def list_to_str(s):
    str1 = " "

    for ele in s:
        str1 += ele

    return str1
print(list_to_str(["Driver", "code"]))

#2 Using .join() method
def list_to_str(s):
    str1 = " "
    return str1.join(s)

print(list_to_str(["Driver", "code"]))

# 3  Using list comprehension
s = ['I', 'want', 1, 'apple', 'and', 3, 'oranges']

list_to_str = ' '.join([str(elem) for elem in s])

print(list_to_str)

# 4 using map
s = ['I', 'want', 4, 'apples', 'and', 2, 'bananas']
print(' '.join(map(str, s)))
