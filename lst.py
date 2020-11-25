# You are given a space separated list of integers.
# If all the integers are positive, then you need to check if any integer is a palindromic integer.
n = int(input())
nums = input().split()
print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums))
# or
print(all([i>0 for i in nums]) and any([str(j)==str(j)[::-1] for j in nums]))
#or
print(all(map(lambda x:x>0,nums)) and any(map(lambda x:str(x)==str(x)[::-1],nums)))

# write a program that returns a list that contains only the elements that are common between the lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a+b:
    if i not in c:
        c.append(i)
print(c)
#or
b = [1,3,3,3,3,3,3,3,3,3,3,3]
a = [1, 2, 3, 4, 5, 6, 7, 8, 21]
new_list = []
for num in a:
    if num in b:
        new_list.append(num)
print(new_list)
