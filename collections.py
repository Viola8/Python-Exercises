# Write a Python program to get the frequency of the elements in a list.
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
freq = collections.Counter(my_list)
print("Frequency of the elements in the List : ",freq)

# Write a Python program to find all anagrams of a string in a given list of strings using lambda.

from collections import Counter
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print(list(filter(lambda x: (Counter(str) == Counter(x)), texts)))

# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d) # Counter({'b': 400, 'd': 400, 'a': 400, 'c': 300})

# Write a Python program to find the highest 3 values in a dictionary.
from collections import Counter
d3 = {'a': 12, 'b': 24, 'c':36, 'd':48, 'e':60, 'f':72}
k = Counter(d3)
high = k.most_common(3)  # Finding 3 highest values
for i in high:
    print(i[0]," :",i[1]," ")
# Output:
# f  : 72
# e  : 60
# d  : 48
