# Write a Python program to get the largest number from a list.

# with SORT()
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])

# with MAX()
list2 = [30,40,67]
print(max(list2))

# with function
def myMax(list1):
    max = list1[0] # Assume first number in list is largest
    # initially and assign it to variable "max"

    for x in list1:# Now traverse through the list and compare
        if x > max :# each number with "max" value. Whichever is largest assign that value to "max'.
             max = x
    return max # after complete traversing the list return the "max" value
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))
