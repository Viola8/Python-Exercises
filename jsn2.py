# Write a Python program to convert Python dictionary object (sort by key) to JSON data.
# Print the object members with indent level 4.
import json
j_str = {'Nick': 5, 'Luck': 7, 'Michele': 3, 'Alice': 4}
print(j_str)
print(json.dumps(j_str, sort_keys=True, indent=4))

# Write a Python program to convert JSON encoded data into Python objects.
jobj_dict =  '{"Year": 2021, "Month": "June", "Day": 29}'
jobj_list =   '["Happy", "Glad", "Nice"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
print(json.loads(jobj_dict))
print(json.loads(jobj_list))
print(json.loads(jobj_string))
print(json.loads(jobj_int))
print(json.loads(jobj_float))

# Write a Python program to access only unique key value of a Python object.
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print(python_obj)
print(json.loads(python_obj)) # Output: {'a':  4, 'b': 2}
