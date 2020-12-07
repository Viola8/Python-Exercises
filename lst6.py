# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
color =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

list1 = [11, 5, 17, 18, 23, 50]

unwanted = [0, 3, 4] # given index of elements removes 11, 18, 23

for ele in sorted(unwanted, reverse = True):
    del list1[ele]

print (*list1) # printing modified list

#Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).

list1 = [1,4,5,6,5,8,9,4,12,11,12,10,12]

list2 = []

for i in list1:
    list2.append(i**2)

print(list2[:5])
print(list2[-5:])
