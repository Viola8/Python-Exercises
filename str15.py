# Write a Python function to create the HTML string with tags around the word(s). Go to the editor
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'

def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

OUTPUT: John is 23 years old.
