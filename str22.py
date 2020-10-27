# Write a Python program to sort a string lexicographically.

def sorted_string(str1):
    return ''.join(sorted(str1))

print(sorted_string("school"))

# OUTPUT: chloos


def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('school'))

# OUTPUT: ['c','h','l','o','o','s']
