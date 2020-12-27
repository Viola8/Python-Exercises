# Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
dic = dict()
for i in range(1,16):
    dic[i] = i*i
print(dic) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# Write a Python script to merge two Python dictionaries.
# 1
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3 = {}
for i in d1,d2:
    d3.update(i)
print(d3) # {'x': 300, 'y': 200, 'a': 100, 'b': 200}
# 2
d = d1.copy()
d.update(d2)
print(d) # {'x': 300, 'y': 200, 'a': 100, 'b': 200}
# 3
d3 = {**d1, **d2} #  ** a single expression is used to merge two dictionaries and stored in a third dictionary.
print(d3) # {'x': 300, 'y': 200, 'a': 100, 'b': 200}

# Write a Python program to sum all the items in a dictionary.
d = {'a': 10, 'b': 20, 'b': 30}
print(sum(d.values())) # output: 40
