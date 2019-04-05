# base/parent class
class Person:

    def __init__(self, name='Reginald'):
        print('Creating new Person with name:', name)
        self.name = name

    def greet(self):
        print('Hello, I am ', self.name)

    def laugh(self):
        print("Ha ha ha!")

# derived/child class
class Comedian(Person):

    def __init__(self, name):
        # We can call the init method of the parent/super class, Person, if we want
        # to use its init behaviour - here it saves us from writing 'self.name = name' again.
        # Note that we have to pass in both 'self' and 'name' when call it this way
        Person.__init__(self, name)

        # Here is another way you can call the init method of the parent class;
        # it has the same effect and you might see it in other code.
        # Note that with this version we don't need to pass in 'self'
        #
        # super().__init__(name)

        # Then we can add our own custom init code which is JUST for Comedians.
        # Note that if we don't want to add any custom code, we're better off
        # NOT defining our own version of __init__ for Comedian at all; in that
        # case, the version of __init__ in the parent class Person will just be
        # used automatically
        print('Creating new Comedian with name', name)



    def tell_joke(self):
        print('Knock knock...')

    def laugh(self):
        # Another example of calling the parent class' version of a method
        Person.laugh(self)

        # And the alternate way of doing it:
        # super().laugh()

        # Additional code just for comedians goes here:
        print("I'm going to steal that one.")




# Instantiate some new objects using this class!

frederick = Person('Frederick')
frederick.greet()
frederick.laugh()

reg = Person()
reg.greet()
reg.laugh()

stew = Comedian('Stewart')
stew.greet()     # This will use the greet() method defined in the parent Person class
stew.laugh()     # This will use our overridden version of laugh() defined in Comedian
stew.tell_joke() # This method is ONLY defined for Comedian objects, not Person objects
