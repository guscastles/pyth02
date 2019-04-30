employees = [
  {
    "first_name": "Bill",
    "last_name": "Lumbergh",
    "job_title": "Vice President",
    "hire_date": 1985,
    "performance_review": "excellent"
  }, {
    "first_name": "Michael",
    "last_name": "Bolton",
    "job_title": "Programmer",
    "hire_date": 1995,
    "performance_review": "poor"
  }, {
    "first_name": "Peter",
    "last_name": "Gibbons",
    "job_title": "Programmer",
    "hire_date": 1989,
    "performance_review": "poor"
  }, {
    "first_name": "Samir",
    "last_name": "Nagheenanajar",
    "job_title": "Programmer",
    "hire_date": 1974,
    "performance_review": "fair"
  }, {
    "first_name": "Milton",
    "last_name": "Waddams",
    "job_title": "Collator",
    "hire_date": 1974,
    "performance_review": "does he even work here?"
  }, {
    "first_name": "Bob",
    "last_name": "Porter",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }, {
    "first_name": "Bob",
    "last_name": "Slydell",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }
]

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
