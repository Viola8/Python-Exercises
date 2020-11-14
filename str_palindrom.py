# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# good only for a word:

user_string = (input("Please write a string: ")

new_string=user_string[::-1]

if new_string == user_string:
    print("Wow! This is a palindrom!")
else:
    print("Thank you for the participation!")
