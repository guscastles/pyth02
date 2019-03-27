
# Pseudocode:
#
# 1. make up a secret number
# 2. keep track of the user's answer in a variable
# 3. ask the user for their guess
# 4. keep asking the user for their guess until they guess correctly
# 5. print a congratulatory message

secret_number = 5
user_guess = int(input('Please enter a guess: '))

while secret_number != user_guess:
    # keep asking the user for their guess
    user_guess = int(input('Wrong! Guess again: '))

# print congratulatory message
print('Correct! You are the Numberwang champion.')
