students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in range(len(students)):
    print students[i]["first_name"], students[i]["last_name"]


users = {
 'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students"
# for students in users.items():
for i in range(len(users['students'])):
    length = len(users['students'][i]['first_name']) + len(users['students'][i]['last_name'])
    print '{} - {} {} - {}'.format(i, users['students'][i]['first_name'], users['students'][i]['last_name'], length) 
print "Instructors"
for i in range(len(users['instructors'])):
    length = len(users['instructors'][i]['first_name']) + len(users['instructors'][i]['last_name'])
    print '{} - {} {} - {}'.format(i, users['instructors'][i]['first_name'], users['instructors'][i]['last_name'], length) 