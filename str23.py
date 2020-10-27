# Remove unwanted characters from string.

#1.  Using replace()
bad_char = ["*"]
test_string = "Great*news!"

for i in bad_char:
    test_string = test_string.replace(i, '')

print ("Resultant list is : " + str(test_string))  # Output: Great news!

#2. Using join() + generator
bad_chars = [';', ':']
test_string = "Check; this: code:"

test_string = ''.join(i for i in test_string if not i in bad_chars)

print ("Resultant list is : " + str(test_string)) # Output: Check this code

#3. Using translate()
import string

bad_chars = [';', ':', "*"]
test_string = "Good; to* know:!"

delete_dict = {sp_character: '' for sp_character in string.punctuation}
delete_dict[' '] = ''
table = str.maketrans(delete_dict)
test_string = test_string.translate(table)

print ("Resultant list is : " + str(test_string)) # Output: Goodtoknow

#4. Using filter()
bad_chars = ['&', "*"]

test_string = "Good*& luck!"

test_string = ''.join((filter(lambda i: i not in bad_chars, test_string)))

print("Resultant list is : " + str(test_string)) #Output: Good luck!
