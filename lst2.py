 # Write a Python function that takes two lists and returns True if they have at least one common member.
def lst_compare(list1,list2):
    for i in list1:
        if i in list2:
            return True
print(lst_compare([1,2,3],[1,2]))

print(lst_compare([1,2,3],[4,5]))

# write a program that prints out all the elements of the list that are less than 5 and 14.
a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list=[]

for a in a_list:
    if a < 14:
        new_list.append(a)

print(new_list)
print([a for a in a_list if a<5]) # a = output, item = a, list, filter = a < 5

#  Write a Python program to check a list is empty or not.
a = [1,2,3]

if len(a) == 0:
    print("The list is empty!")
else:
    print("The list is not empty :)")

#or
b = [] # Empty lists evaluate to False
if not b:
    print ("The list b is empty")
else:
    print ("list is not empty")
