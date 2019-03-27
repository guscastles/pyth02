
classmates = ['Jalal', 'Adria', 'Emily', 'Snoxy', 'Aleks']

# counter = 0
#
# for each_name in classmates:
#     print('Item #', counter)
#     print('Item using []:', classmates[counter] )
#     print('Hello, ', each_name.upper(), '!', sep='')
#
#     # change the value in the current counter position of classmates
#     classmates[counter] = each_name.upper()
#
#     # counter = counter + 1
#     counter += 1
#
# print(classmates)


## Using range():
# for i in range( len(classmates) ):
#     print( 'i:', i )
#     print( classmates[i] )
#     classmates[i] = classmates[i].upper()
#
# print(classmates)

# Using enumerate(list):
for index, item in enumerate(classmates):
    print(index, item)
    classmates[index] = item.upper()

print(classmates)
