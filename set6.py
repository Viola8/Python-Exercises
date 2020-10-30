
# d=5
# a = 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# only 8 is unique in this set

d=(input())  #get rid of first line
a=(input())  #store all to array
s1=set()  #all unique room number
s2=set()  #all unique room number occur more than once
for i in a:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)

print(list(s1.difference(s2)))
