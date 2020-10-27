# Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form (alphanumerically).

sentence = "red", "white", "black", "red", "green", "black"

list_of_words = set(sentence)

print(sorted(list_of_words))
# OUTPUT: ["black", "green", "red", "white"]

# N2

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

# INPUT: noire, rougem jaune OUTPUT: jaune, noir, rouge

# Write a Python script that takes input from the user and displays that input back in upper and lower cases.

user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())

# OUTPUT FRENCH  french
