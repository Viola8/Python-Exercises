# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d) # Counter({'b': 400, 'd': 400, 'a': 400, 'c': 300})

# Write a Python program to print all unique values in a list of dictionary.
lst = [{"V":"001"}, {"V": "002"}, {"VI": "001"}, {"VI": "005"}, {"VII":"005"}, {"V":"009"},{"VIII":"007"}]
print(set( val for dic in lst for val in dic.values())) # {'009', '002', '007', '005', '001'}

# Write a Python program to find the highest 3 values in a dictionary.
from heapq import nlargest
d3 = {'a': 12, 'b': 24, 'c':36, 'd':48, 'e':60, 'f':72}
three_largest = nlargest(3, d3, key=d3.get)
print(three_largest) # ['f', 'e', 'd']
# 2
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
