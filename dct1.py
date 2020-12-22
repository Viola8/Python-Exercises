# Sort (ascending and descending) a dictionary by value.
dct = {'Oscar': 2, 'Michael': 4, 'Ana': 3, 'Seth': 1, 'John': 0}
print(dict(sorted(dct.items(), key = lambda item: item[1])))
print(dict(sorted(dct.items(), key = lambda item: item[1], reverse=True)))

# Write a Python script to add a key to a dictionary.
# 1
d =  {0: 10, 1: 20}
d.update({2:30})
print(d) # {0: 10, 1: 20, 2: 30}
# 2
d[3] = 40
print(d) # {0: 10, 1: 20, 2: 30, 3: 40}
# 3
d.__setitem__(4,50)
print(d) # {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}
# 4
dict = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}
new_dict = {**dict, **{5: 60}}
print(new_dict) # {0: 10, 1: 20, 2: 30, 3: 40, 4: 50, 5: 60}

# Write a Python script to check whether a given key already exists in a dictionary.
dct = {'Oscar': 2, 'Michael': 4, 'Ana': 3, 'Seth': 1, 'John': 0}
print(dct['Oscar']) # output: 2
print('Ana' in dct) # True
print(dct.get('Seth')) # output: 1
print(dct.get("Mike")) # None

def check_key(k):
    if k in dct:
        print("Key is present in this dictionary")
    else:
        print("Key is not present in this dictionary")
check_key("Michael")
check_key("Viola")
