
student = [
    'Bazza McGonnagal', # name
    25, # age
    '12 Test St', # address
    90 # test score
]

# print out name:
print('name:', student[0] )
print('address:', student[2] )

student_dictionary = {
    'name': 'Bazza McGonnagal',
    'age': 25,
    'address': {
        'street': '12 Test St',
        'postcode': '2000',
        'suburb': 'Sydney',
    },
    'scores': [70, 80, 60, 90, 100]
}

print('name:', student_dictionary['name'])
print('age:', student_dictionary['age'])
# nested dictionary access:
print('street address:', student_dictionary['address']['street'])
print('postcode:', student_dictionary['address']['postcode'])
# list as value of key, access first element:
print('first score:', student_dictionary['scores'][0])
