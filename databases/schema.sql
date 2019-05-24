CREATE TABLE employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- take care of IDs internally
    first_name TEXT,
    last_name TEXT,
    job_title TEXT,
    hire_date DATETIME,
    performance_review TEXT
);
