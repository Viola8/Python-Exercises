
# Find a list of uncommon words in two strings.
def UncommonWords(A, B):

    count = {} # count will contain all the word counts

    for word in A.split():
        count[word] = count.get(word, 0) + 1 # insert words of string A to hash

    for word in B.split():
        count[word] = count.get(word, 0) + 1 # insert words of string B to hash

    return [word for word in count if count[word] == 1] # return required list of words

print(UncommonWords("Geeks for Geeks", "Learning from Geeks for Geeks")

# Also another way-using in-built function “symmetric_difference()”
def uncommon(a,b):
  a=a.split()
  b=b.split()
  k=set(a).symmetric_difference(set(b))
  return k

#Driver code
if __name__=="__main__":
  a="apple banana mango"
  b="banana fruits mango"
  print(list(uncommon(a,b)))
