# Output the integer number indicating the total number of occurrences of the substring in the original string.

string = "ABCDCDCDCDC"
substring = "CDC"

count=0
for i in range(len(string)):
    if string[i:].startswith(substring):
        count+=1
print(count)

#Output: 4
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count
print(count_substring("mamamamamamamamamaaa","ma"))
#    or

def count_substring(string, sub_string):
        count = 0
        for i in range(len(string)):
                count += string.startswith(sub_string, i)
        return count
print(count_substring("dododododddddooodododod","do"))
# startswith(value, start, end)
# startswith(sub_string,i) - i = start
