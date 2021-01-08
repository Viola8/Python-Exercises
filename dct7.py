# Write a Python program to create a dictionary from a string.
from collections import defaultdict, Counter
str1 = "dictionary"

my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# Write a Python program to print a dictionary in table format.
dct = {'1':[1,2,3],'2':[1,2,3],'3':[1,2,3]}
for row in zip(*([key] + (value) for key, value in sorted(dct.items()))):
    print(*row)
# Output:
# 1 2 3
# 1 1 1
# 2 2 2
# 3 3 3

# Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True},
 {'id': 2, 'success': False},
 {'id': 3, 'success': True},{'id': 4, 'success': True}]
print(sum(d['id'] for d in student)) # 10
print(sum(d['success'] for d in student)) # 3
