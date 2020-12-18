# Write a Python program to sort a list of tuples using Lambda.

subjects = [('English', 99), ('Science', 90), ('Maths', 98), ('Social sciences', 85)]
subjects.sort(key = lambda x: x[1])
print(subjects)

# or
print(sorted(subjects, key = lambda x: x[1]))

# to sort a list of dictionaries using Lambda.
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print(sorted(models, key = lambda x: x['color']))

# to rearrange positive and negative numbers in a given array using Lambda.
array_nums = [-5,-2, -3, 5, 7, 14, 9, -10]
print(sorted(array_nums, key = lambda x: 0 if x == 0 else -1/x)) # [5, 7, 14, 9,-10,-5,-3,-2]

# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
lst = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(list(filter(lambda x: x % 19 == 0 or x % 13 == 0, lst))) # [19, 65, 57, 39, 152, 190]

# to find palindromes in a given list of strings using Lambda.
lst = ['php', 'Pytorch', 'Python', 'nltk', 'gensim', 'aaa']

print(list(filter(lambda i: i == "".join(reversed(i)), lst))) # ['php', 'aaa']
