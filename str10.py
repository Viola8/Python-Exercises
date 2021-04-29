# change a given string to a new string where the first and last chars have been exchanged.
def str_char_exchange(s):
    list1 = list(s)
    list1[0], list1[-1] = list1[-1], list1[0]
    s = ''.join(list1)
    return s
print(str_char_exchange("abcd"))

# or just return = ''.join(list1)



#or using slices and indexes:
# universal
def swap(s, i, j):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))

print(swap('abcde', 1, 3))
# Output: 'adcbe'

# for only first and last indexes:

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]

print(change_sring('abcd'))
print(change_sring('12345'))
