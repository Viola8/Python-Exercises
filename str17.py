# Write a Python function to get a string made of 4 copies
# of the last two characters of a specified string (length must be at least 2).

def ending_copy(word):
    if len(word)<2:
        return
    else:
        return word[-2:] * 4
print(ending_copy("n"))

# OUTPUT: None

print(ending_copy("Python"))

# OUTPUT: onononon
