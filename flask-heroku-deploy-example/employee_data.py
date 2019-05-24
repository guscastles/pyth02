# employees = [
#   {
#     "first_name": "Bill",
#     "last_name": "Lumbergh",
#     "job_title": "Vice President",
#     "hire_date": 1985,
#     "performance_review": "excellent"
#   }, #...etc....
# ]


# This code will run whenever the module is loaded (but only once!)
import csv

# Load the CSV file into our list 'employees'.
# We need to use list() to force the csv code to actually read in the contents of
# the file, otherwise it will 'lazy' load it on first access of the employees list
# element, by which time the file will be closed.
with open('employees.csv') as csv_file:
    employees = list( csv.DictReader(csv_file) )


def save_employees():
    # save our (modified) employees list back to the CSV!
    with open('employees.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['first_name', 'last_name', 'job_title', 'hire_date', 'performance_review'])
        writer.writeheader()
        writer.writerows(employees)



def check_employee_match(emp, search_query):
    return (
      search_query in emp['first_name'].lower() or
      search_query in emp['last_name'].lower()  or
      search_query in emp['job_title'].lower()  or
      search_query in str(emp['hire_date'])
    )

def search(query_string):
    results = []
    for employee in employees:
        if check_employee_match(employee, query_string):
            results.append( employee )

    # list comprehension version:
    # results = [ emp for emp in employee_data.employees if check_employee_match(emp, query) ]

    return results
