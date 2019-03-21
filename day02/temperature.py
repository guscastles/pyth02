
# temperature = 70
temperature = input('What is the temperature? ')

# convert from input string to integer
temperature = int(temperature)

if temperature > 80:
    print("It's too hot!")
elif temperature < 40:
    # The elif is only reached when the preceding
    # if condition is false
    print("It's too cold. Frostbite much?")
else:
    # The else block only runs when none of the
    # above if/elif tests are true
    print("It's just right.")


# The following line is not indented, so it is not
# involved with the above conditional tests at all,
# i.e. it always runs
print("Thank you for using this program.")
