# The simpliets solution witj JOIN method. It doesn't work with integers!!!
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

# with list comprehension
list1 = [2,'apple','45']

str1 = ' '.join([str(ele) for ele in list1])

print(str1)
# with function and a new str. It doesn't work with integers!!!

def lstToStr(list2):
    str2 = ""
    for ele in list2:
        str2 += ele
    return str2
print(lstToStr(['plums','banana','kiwi']))

# with a new str and JOIN method:
def lstToStr2(list3):
    str3 = ""
    return str3.join(list3)

print(lstToStr2(['Sergei','Dima','Letka']))

# with MAP function and a list comprehension
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

listToStr = ' '.join(map(str, s))
print(listToStr)
