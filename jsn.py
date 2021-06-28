# Write a Python program to convert JSON data to Python object.
import json
json_obj =  '{ "Name":"David", "Language":"English", "Country":"US" }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(json_obj)
print("\nName: ",python_obj["Name"])
print("Language: ",python_obj["Language"])
print("Country: ",python_obj["Country"])

 # Write a Python program to convert Python object to JSON data.
python_obj = {
  "Name": "Charles",
  "Language":"French",
  "Country": "France"
}
print(type(python_obj))  # Output: <class 'dict'>
j_data = json.dumps(python_obj) # convert into JSON.
print(j_data) # result is a JSON string.

# Write a Python program to convert Python objects into JSON strings. Print all the values.
python_dict =  {"Name": "Vladimir", "Language": "Russain", "Country":"Russia"}
python_list =  ["June", "July", "August"]
python_str =  "Python Json"
python_int =  (888)
python_float =  (08.08)
python_T =  (True)
python_F =  (False)
python_N =  (None)

print(json.dumps(python_dict))
print(json.dumps(python_str))
print(json.dumps(python_int))
print(json.dumps(python_float))
print(json.dumps(python_T))
print(json.dumps(python_F))
print(json.dumps(python_N))
