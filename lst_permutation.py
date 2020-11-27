# with direct function
from itertools import permutations
l = list(permutations(range(1, 4)))
print (l)

# with resursion
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are more than 1 characters
    l = [] # empty list that will store current permutation

    for i in range(len(lst)): # Iterate the input(lst) and calculate the permutation
       m = lst[i]

       remLst = lst[:i] + lst[i+1:] # Extract lst[i] or m from the list.  remLst is remaining list

       # Generating all permutations where m is first element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

print(permutation([1,2,3]))
