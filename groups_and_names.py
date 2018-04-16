# part 1
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for student in students:
#   print student["first_name"] + " " + student["last_name"]

# part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for user in users:
  print user
  count = 1
  for student in users[user]:
    first = student["first_name"].upper()
    last = student["last_name"].upper()
    length = len(student["first_name"]) + len(student["last_name"])
    print count, "- " + first + " " + last + " -", length
    count += 1
  count = 1

# for student in students:
# print student["first_name"] + " " + student["last_name"]

