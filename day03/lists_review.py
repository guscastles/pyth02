
# 1. Declare a list with the names of your classmates
classmates = ['Jalal', 'Adria', 'Emily', 'Snoxy', 'Aleks']

# 2. Print out the length of that list
print( 'list length:', len(classmates) )

# 3. Print the 3rd name on the list
print( 'third item:', classmates[2] )

# 4. Delete the first name on the list
first_name = classmates.pop(0)
print( 'list:', classmates )
print( 'first_name:', first_name )

# 5. Re-add the name you deleted to the end of the list
classmates.append( first_name )
print( 'list:', classmates )
