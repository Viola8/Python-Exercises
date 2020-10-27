# count the occurrences of each word in a given sentence.

def word_counter(sentence):

    counter = {}
    words = sentence.split()

    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] +=1
    return counter
print(word_counter("one deep night occured this nigth"))

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy lazy lazy dog.'))
