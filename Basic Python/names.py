users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
    }

def names(dict):
    for person, data in users.iteritems():
        print person
        # print data
        keyOne = 0
        for count in data:
            keyOne += 1
            keyTwo = len(count["first_name"]) + len(count["last_name"])
            print keyOne , " - " , count["first_name"].upper() , " " , count["last_name"].upper() , " - " , keyTwo 

names(users)