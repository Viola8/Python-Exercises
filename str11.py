str1 = 'Python'
for i in range(len(str1)):
    if i % 2 ==0:
        print(i)
# Output 0 2 4

def str_rem(str2):
    result = " "
    for i in range(len(str2)):
        if i % 2 == 0:
            result += str2[i]
    return result
print(str_rem('Python'))
