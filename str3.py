# Write a Python program to convert the given string to list.
str1 = "Convert a string to a list"
print(str1.split())

def Convert_str_to_lst(string):
    lst = list(string.split(" "))
    return lst
str1 = "Convert a string to a list"
print(Convert_str_to_lst(str1))

# 2
def Convert_str_to_lst(string):
    lst = list(string.split("-"))
    return lst
str1 = "Convert-a-string-to-a-list"
print(Convert_str_to_lst(str1))

# 3
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

str1="ABCD"
print(Convert(str1))
