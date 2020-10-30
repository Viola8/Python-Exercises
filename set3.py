# symmetric_differencer returns a set that contains all items from both sets, except items that are present in both sets
set_a = set(input().split())


set_b = set(input().split())

c = sorted(list(set_a.symmetric_difference(set_b)))

for i in c:
    print (i)
