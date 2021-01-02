# Write a Python program to get the maximum and minimum value in a dictionary.
dct = {'Oscar': 21, 'Michael': 26, 'Ana': 39, 'Seth': 15, 'John': 50}
# 1 with values()
all_values = dct.values()
print(max(all_values)) # 50
print(min(all_values)) # 15

# 2 with keys()
key_max = max(dct.keys(), key=(lambda k: dct[k]))
key_min = min(dct.keys(), key=(lambda k: dct[k]))
print(dct[key_max]) # 50
print(dct[key_min]) # 15

# Write a Python program to get a dictionary from an object's fields.
class creat_dict():
    def __init__(self):
        self.a = 'new'
        self.b = 'young'
        self.c = 'smart'
        self.d = 'great'
test = creat_dict()
print(test.__dict__) # {'a': 'new', 'b': 'young', 'c': 'smart', 'd': 'great'}

# Write a Python program to check a dictionary is empty or not.
dct = {'Oscar': 2, 'Michael': 4, 'Ana': 3, 'Seth': 1, 'John': 0}
empty_dct = {}

print(not dct) # False
print(not empty_dct) # True

print(not bool(dct)) # False
print(not bool (empty_dct)) # True
