# Write a Python program to find the values of length six characters in a given list using Lambda.

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

result = list(filter(lambda day: day if len(day) == 6 else '', weekdays))
print(result) # ['Monday', 'Friday', 'Sunday']

# Write a Python program to add two given lists using map and lambda. Go to the editor
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list(map(lambda x,y: x + y, list1, list2))) # [5, 7, 9]
print(list(map(lambda x,y: list1 + list2, list1, list2))) # [1, 2, 3, 4, 5, 6]

# To find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda.

students = [['Ramberg', 1.0], ['Larose', 3.0], ['Holmes', 2.0], ['Ghosh', 1.0], ['McBride', 1.0]]

order = sorted(students, key = lambda x: int(x[1]))
for i in range(len(students)):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ", second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nName:")
for s_name in sec_student_name:
   print(s_name)
