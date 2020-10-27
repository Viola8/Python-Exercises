# Write a Python function to reverses a string if it's length is a multiple of 4.

def str_mult_of_4(str1):
    if len(str1)%4 == 0:
        return str1[::-1]
print(str_mult_of_4('Ruby'))

# OUTPUT: ybuR

print(str_mult_of_4('Viola'))

# OUTPUT: None

# or with reversed function

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))  # функция для СПИСКА применима для строки с ''.join !!!! без отдельного перевода строки в список
    return str1

print(reverse_string('abcd'))
print(reverse_string('Python'))

# reversed function Reverse the sequence of a LIST !!!, and print each item

# OUTPUT: dcba & Python
