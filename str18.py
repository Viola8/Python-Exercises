# Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string.

def new_string(str1):
    if len(str1) < 3:
        return str1
    else:
        return str1[:3]
print(new_string("Python"))

# OUTPUT: Pyt

print(new_string("Vi"))

# OUTPUT: Vi
