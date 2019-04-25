
from flask import Flask, render_template

import employee_data  # Load our own data file as a module

app = Flask(__name__)


# Route definitions
@app.route('/')
def index():
    return 'Please visit <a href="/employees">/employees</a> to start using this app.'

# Index of Employees
@app.route('/employees')
def employee_index():

    # print( employee_data.employees )
    return render_template('employees.html', employees=employee_data.employees)


# Start the server (only if not running from a module)
if __name__ == '__main__':
    app.run(debug=True)
