# Write a Python program to get the difference between the two lists.
list1 = [1,2,3,4,5,6,7]
list2 = [2,3,4,8,9]

for i in list1:
    if i not in list2:
        print(i)
#or
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)

# Write a Python program to remove duplicates from a list.
list1 = [1,2,3,4,4,5,5,5]
set_list1 = set(list1)

print(list(set_list1))

#or

a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
