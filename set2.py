#union returns a set that contains all items from both sets, duplicates are excluded

set_n = set(input().split())

set_b = set(input().split())
print(len(set_n.union(set_b)))
