
def divides(numerator, divisor):
    return numerator % divisor == 0

def fizz_buzz(number):
    if divides( number, 15 ):
        print('FizzBuzz')
    elif divides( number, 3 ):
        print('Fizz')
    elif divides( number, 5 ):
        print('Buzz')
    else:
        print(number)


for num in range(1, 101):
    fizz_buzz( num )

# fizz_buzz(45)
