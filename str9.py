def rem_index(word,n):
    first_part = word[:n] # last index is exclusif
    second_part = word[n+1:] # this part of code is very similar to string permutaion

    return first_part+second_part # we exclude n
print(rem_index('NLTK',1))  # Output: NTK
print(rem_index('NLTK',3)) # Output: NLT
