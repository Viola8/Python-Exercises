# Write a Python program to sort each sublist of strings in a given list of lists using lambda.
lst = [['orange','green'], ['black', 'white'], ['white', 'black', 'orange']]

ordered_sublists = [sorted(w,key = lambda w: w[0]) for w in lst]
print(ordered_sublists) # [['green', 'orange'], ['black', 'white'], ['black', 'orange','white']]

# Write a Python program to sort a given list of lists by length and value using lambda.
lst2 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print(sorted(lst2, key = lambda l: (len(l), l))) # [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# Write a Python program to find the maximum value in a given heterogeneous list using lambda.
list1 = ['Python', 3, 2, 4, 5, 'version']
print(max(list1, key = lambda w: (isinstance(w, int), w))) # output: 5

# Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
list2 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
list3 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(sorted(list2, key=lambda i: sum(i)))
print(sorted(list3, key=lambda i: sum(i)))

# Write a Python program to extract specified size of strings from a give list of string values without lambda and with Lambda.
list4 = ['Python', 'list', 'exercises', 'practice', 'solution']
# without lambda
extracted_words = []
for w in list4:
    if len(w)==8: # length of the string to extract is 8
        extracted_words.append(w)
print(extracted_words) # ['practice', 'solution']
# with lambda
print(list(filter(lambda x: len(x) == 8, list4))) # ['practice', 'solution']
