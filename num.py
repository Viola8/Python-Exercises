# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.


num = int(input("Please tell a number: "))
if num%4==0:
    print("Your number is multiple of 4")
elif num%2==0:
    print("Your number is even")
else:
    print("Your number is odd")

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num_2 = int(input("Please enter a number: "))
check = int(input("Please enter another number to devide the previous one: "))


if num_2%check==0:
    print("Your second number devided evently into the fisrt number")
else: print("Your second number didn't devide evently into the fisrt number")
