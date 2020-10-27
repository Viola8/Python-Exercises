# Write a Python function to insert a string in the middle of a string.

def stringInstring(str1, str2):
    x = len(str1)//2
    return str1[:x] + str2 + str1[x:]

print(stringInstring("[[]]", "Python"))

# OUTPUT: [[Python]]

print(stringInstring("{{{{}}}}", "Python"))

# OUTPUT: {{{{Python}}}}
