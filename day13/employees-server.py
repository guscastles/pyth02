
from flask import Flask, render_template, request

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

# Start the server (only if not running from a module)
if __name__ == '__main__':
    app.run(debug=True)
