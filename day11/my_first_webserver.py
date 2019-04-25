
# import the Flask class from the flask library
from flask import Flask, render_template
import random

# create an instance of the Flask class
app = Flask( __name__ )

# Define a route handler for the root route '/', the default route
@app.route('/')
def index():
    return 'Hello World!'  # This is what the browser gets!

# Define a new route handler for the '/aboutus' path
@app.route('/aboutus')
def about():
    # Load an HTML template from the 'templates/' folder and make
    # it the response to this route, by returning it

    random_number =  random.randint(1, 500)

    return render_template('kittens.html', random_number=random_number )
    # return "Your random number is: " + str( random.randint(1, 500) )

# We don't want to have to write a separate routing rule and handler
# for every variation of a range of possible URLS, like this:
# @app.route('/say/hello')
# def hello():
#     return "hello"
#
# @app.route('/say/goodbye')
# def goodbye():
#     return "goodbye"

# Dynamic route: any URL that starts with '/say/' and then a string
# will be capture by this routing rule because of the '<variable-name>'
# syntax. We also need to define it as an argument to our handler function,
# and then we can use it like any variable.
# DOES NOT MATCH: '/say', '/say/' or '/say/something/somethingelse'
@app.route('/say/<thing_to_say>')
def sayer(thing_to_say):
    return "You asked me to say: " + thing_to_say


@app.route('/adder/<x>/<y>')  # calls adder(x=100, y=111)
def adder(x, y):

    sum = int(x + y)

    # return "You entered: {x} and {y}, sum = {sum} ".format(x=x, y=y, sum=sum)
    return render_template('adder-result.html', x=x, y=y, sum=sum)


# start app only if this file is being run directly,
# and not loaded as a module
if __name__ == '__main__':
    app.run( debug=True )
