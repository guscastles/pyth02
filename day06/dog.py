
class Dog:

    # class variable, whose value is shared by all objects created from this class
    dog_count = 0

    # constructor function for this class:
    # this is what runs when you type:  d = Dog('Fido', 7)
    def __init__(self, name, roundness):

        # You have to do your own type checking in Python!
        # if not type(name) == str:
        #     raise TypeError, 'Please use a string for "name"'

        print('Creating a new instance of Dog:', name, roundness)

        # Increment the class variable: note that we do this via the class name,
        # NOT via self
        Dog.dog_count += 1

        # 'Instance variables'/attributes - each object gets its own copy of these
        # Here we just set them from the arguments passed to this init (constructor) function
        self.name = name
        self.roundness = roundness

    # Every method of a class MUST have 'self' as its first argument, even if you
    # don't use it in the body of the method (try leaving it out and see what happens)
    def describe(self):
        print('Name of dog', self.name)
        print('Roundness of dog', self.roundness)

    # Methods can have default values for parameters just like normal functions,
    # as well as variable length arguments (*args), keyword arguments (**kwargs), etc
    def bark(self, bark_count=1):
        bark_output = "Woof! I am " + self.name + ' '
        print(bark_output * bark_count)  # multiple copies of a string using '*'


fido = Dog('Fido', 7)
rex = Dog('Rex', 2)
