
input_string = '123'

def digits_to_words(str):

    digit_lookup = {
        '1': 'one',
        '2': 'two',
        '3': 'three'
    }

    output = ''

    for char in str:
        # if char == '1':
        #     output += 'one '
        # elif char == '2':
        #     output += 'two '
        # elif char == '3':
        #     output += 'three '
        output += digit_lookup[char] + ' '
        # print(char, output)
        # print(vars())



    return output


print('input:', input_string)
print('output:', digits_to_words(input_string))
