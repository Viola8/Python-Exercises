# Write a Python program that multiply each number of given list with a given number using lambda function. Print the result. Go to the editor
lst = [2, 4, 6, 9, 11]
x = int(input())
print(list(map(lambda y: y*x, lst)))

# or
nums = [2, 4, 6, 9, 11]
n = 3
result = list(map(lambda number:number*n,nums))
print(result)

# sum the length of the names of a given list of names after removing the names
# that starts with an lowercase letter. Use lambda function.
names = ['denna', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'kilian', 'George']
names = (list(filter(lambda name: name[0].isupper(), names)))
print(names)                # [Dylan', 'Diana', 'Joanne', 'George']
print(len(' '.join(names))) # 25

# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
lst = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print(sum(list(filter(lambda x: x > 0, lst)))) # 48
print(sum(list(filter(lambda x: x < 0, lst)))) # -32

# to find the list with maximum and minimum length using lambda.
lst = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

max_length = max(len(x) for x in lst)
max_list = max(lst, key = lambda x: len(x))
print(max_length, max_list)  # 3 [13, 15, 17]

min_length = min(len(x) for x in lst)
min_list = min(lst, key = lambda x: len(x))
print(min_length, min_list)   # 1 [0]
