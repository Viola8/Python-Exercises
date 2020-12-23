# Write a Python script to concatenate following dictionaries.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = {}
for i in dic1,dic2,dic3:
    dic4.update(i)
print(dic4)

# Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30}
for key, value in d.items():
    print(key,'-',value)

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input())
dict1 = {}
for x in range(1,n+1):
    dict1[x] = x*x
print(dict1) #  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} for 5
# Write a Python script to generate a dictionary that contains one key with a value (n*n) .
n = int(input())
dict1 = {}
for x in range(1,n+1):
    dict1[1] = x*x
print(dict1) # {1:25} for 5
