# Write one line of Python that takes this list a and
# makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]

for i in a:
    if i%2==0:
        b.append(i)
print(b)

# in one line - with List Comprehensions:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[i for i in a if i%2==0]
print(b)

# For a solution that uses the random library to generate test lists:
import random

numlist = []
list_length = random.randint(5,15) # длина списка. В него может войти от 5 до 15 случайных чисел

while len(numlist) < list_length:
    numlist.append(random.randint(1,75)) # список забиваем случайными числами

evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)
