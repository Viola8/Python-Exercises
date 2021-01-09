# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
def string_length(a):
    count = 0
    for word in a:
        if len(word) >= 2 and word[0] == word[-1]:
            count +=1
    return count
print(string_length(['abc', 'xyz', 'aba']))   # output: 1

# Write a Python program to count the number of elements in a list within a specified range.

def count_elements(list1, max, min):
    counter = 0
    for ele in list1:
        if max >= ele >=min:
            counter +=1
    return counter
print(count_elements([23,4,12,56,78,69,55,43],56,23)) # output: 4

# Write a Python program to get variable unique identification number or string.
x = 12
str1 = "Id test"
str2 = "Id test"
print(id(x))    # output: 140721336498304
print(id(str1)) # output: 2663592548400
print(id(str2)) # output: 2663592548400
print(id(str1) == id(str2)) # output: True
print(id(str1) == id(x)) # output: False
