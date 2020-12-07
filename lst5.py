def lstmlt(A):
    total = 1
    for i in range(0,len(A)):
        total = total * A[i]
    return total
print(lstmlt([2,4,2]))

#or

def mult_list(A):
  mlt_numbers = 1
  for i in A:
    mlt_numbers *=i
  return mlt_numbers
print(mult_list([2,4,2]))

# Python3 program to multiply all values in the list using numpy.prod()
import numpy
list1 = [1, 2, 3]
list2 = [3, 2, 4]

# using numpy.prod() to get the multiplications
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)
# 2
import math
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = math.prod(list1)
result2 = math.prod(list1)
print(result1)
print(result2)

# using lambda function and reduce()
from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)
