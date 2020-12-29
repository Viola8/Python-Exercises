# Write a Python program to multiply all the values in a dictionary.
dct = {'a':1,'b':2,'c':3}
answer = 1
for key in dct:
    answer = answer * dct[key]
print(answer)

# Write a Python program to remove a key from a dictionary.
# 1 using pop()
dct2 = {'a':2,'b':4,'c':6,'d':8}
dct2.pop("a")
print(dct2) # {'b':4,'c':6,'d':8}
# 2 using del
if 'a' in dct2:
    del dct2['a']
print(dct2) # {'b':4,'c':6,'d':8}

# Write a Python program to map two lists into a dictionary.
keys = ['31', '32', '40']
values = ['Alana','Ben', 'Rodger']
print(dict(zip(keys,values)))

# Write a Python program to sort a dictionary by key.
dct = {'Oscar': 2, 'Michael': 4, 'Ana': 3, 'Seth': 1, 'John': 0}
print(sorted(dct))
