## PYTH02 BONUS HOMEWORK CHALLENGE: Employees DB

1. Display the full details for each employee using the employee list template
1a. Use the `<table>` tag ([docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)) to display the list in a table, a much more spreadsheet-like format.
2. Create a route to perform a free text search on the employee list, like `/employees/search/YOUR-QUERY-HERE`. You should do the searching/filtering in your route handler function (or ideally in a custom search function called by your route handler), and pass the filtered result list to the template. Start by just searching in the `first_name` field for each employee, but then add the other fields too.
3. Work out how to `include` one template from another, so you can re-use the template code that loops through the employees and renders them into an html list or table, by using it to show the search results too. DRY templates!
4. (for the keen) Load the employee list from a CSV instead of hardcoding it in a list of dictionaries (the CSV should still ultimately turn into a list of dictionaries). You can write the code to load the CSV yourself (good data-wrangling practice!), or use the builtin `csv` module.
