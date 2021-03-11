# replace() method is replace() is an inbuilt function in Python programming language
# that returns a copy of the string where all occurrences of a substring is replaced with another substring.
str = "this is string example ... this is really string"
print(str.replace('is','was')) # replace(old, new)
# "thwas was string example ... thwas was really string"
print(str.replace('is','was', 2)) # replace(old, new, count)
# "thwas was string example ... this is really string"

def replacement(input,pattern,replacewith):
    return input.replace(pattern,replacewith)
print(replacement('HelloVWorld', 'V', '_')) # Hello_World
