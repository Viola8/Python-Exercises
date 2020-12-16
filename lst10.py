# Write a Python program to print the numbers of a specified list after removing even numbers from it.
def odd_numbres(list1):
    for i in list1:
        if i % 2 == 0:
            list1.remove(i)

    return list1
print(odd_numbres([1,2,3,4]))

# or
list2 = [2,5,8,9]

num = [x for x in list2 if x % 2 != 0]

print(num)

# Write a Python function that takes a list of words and returns the length of the longest one.
list1 = ['house', 'building', 'patio']

for i in list1:
    print(len(i))
