# Python program to find sum of all elements in list using recursion
lst = [2,2,2]

for i in lst:
    print(sum(lst))

#or
def listsum(N):
    sum_numbers = 0

    for i in N:

        sum_numbers +=i
    return sum_numbers
print(listsum([3,3,3]))

#or with for loop
list1 = [4,4,4]

total = 0

for i in range(0,len(list1)):
    total = total + list1[i]
print(total)

#or with while loop
list1 = [5,5,5]

total = 0
i = 0

while i < len(list1):
    total = total + list1[i]
    i +=1
print(total)

list1 = [11, 5, 17, 18, 23]

# using recursion
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)

# Driver code
total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)
