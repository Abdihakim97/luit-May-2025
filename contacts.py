
contacts = {
    'number': 4,
    'students':
        [
            {'name':'Sarah Holderness','email': 'Sarah@example.com'},
             {'name': 'Harry Potter','email':'herry@example.com'},
              {'name':'Hermione Granger','email':'hermione@example.com'},
              {'name': 'Ron Weasley','email':'ron@example.com'},
        ]
}

print('student emails:')
for students in contacts['students']:
    print(students['email'])


