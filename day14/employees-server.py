
from flask import Flask, render_template, request, redirect, jsonify

import employee_data  # Load our own data file as a module

app = Flask(__name__)


# Route definitions

@app.route('/')
def index():
    return 'Please visit <a href="/employees">/employees</a> to start using this app.'


# Index of Employees
@app.route('/employees')
def employee_index():

    print( employee_data.employees )

    return render_template('employees.html', employees=employee_data.employees)

# Search resuts from query submitted via URL path
@app.route('/employees/search/<query>')
def employee_search(query):
    query = query.lower()
    results = employee_data.search(query)
    return render_template('employees-search-results.html', employees=results, query=query)


# Search results from query submitted via form
@app.route('/employees/search')
def employees_search_form():
    query = request.args['search_text']
    query = query.lower()
    results = employee_data.search(query)
    return render_template('employees-search-results.html', employees=results, query=query)


# Display form for adding a new employee
@app.route('/employees/new')
def employees_new_form():
    return render_template('employees-new-form.html')

# The above form submits to this route:
@app.route('/employees/add', methods=['POST'])
def employees_add():

    # raise
    # from IPython import embed; embed()

    # Create a new employee record (dict) from the submitted form data
    #
    # We need to use 'request.data' and not 'request.args' because
    # our form is being submitted using the POST method now
    new_employee = {
      'first_name': request.form['first_name'],
      'last_name': request.form['last_name'],
      'job_title': request.form['job_title'],
      'hire_date': request.form['hire_date'],
      'performance_review': request.form['performance_review'],
    }

    # Shortcut! SECURITY NIGHTMARE! ANYONE CAN ADD FIELDS TO A FORM
    # ...and this shortcut passes them all through to our employee
    # records without checking if they're allowed!
    # new_employee = request.args.to_dict()

    employee_data.employees.append( new_employee )
    employee_data.save_employees()

    # Redirect to our Employee Index page after we add a new employee
    # (this prevents duplicates being added on reload)
    return redirect('/employees')


    # return render_template('employees.html', employees=employee_data.employees)
    # return '<code>' + repr(new_employee) + '</code>'


# API endpoints!
@app.route('/json/employees')
def employees_index_json():
    return jsonify(employee_data.employees)

# API search results endpoint
@app.route('/json/employees/search/<query>')
def employees_search_json(query):
    query = query.lower()
    results = employee_data.search(query)
    return jsonify(results)

    # a.k.a.
    # return jsonify(employee_data.search(query.lower()))


# Start the server (only if not running from a module)
if __name__ == '__main__':
    app.run(debug=True)
