## Bonus Challenge for Day04: Refactoring using functions with arguments



### Part 1.

Starting with the code from the last challenge (replacing letters with underscores), refactor to create a function called `replace_letters` which does all the work. The function should have the following parameters:
```python
replace_letters(input_string, letters_to_replace, replacement)
```
where:

 - `input_string` is the input string whose characters you want to replace
 - `letters_to_replace` is a either a string OR list of the
   characters to be replaced
 - `replacement` is a string (could be one OR MORE characters)
   which will replace the letters specified in `letters_to_replace`

Your function should not print anything itself, but rather return the
new string, with the specified characters replaced.

Make sure you test your function, making multiple calls with different
arguments, to make sure it works!

Here's an example template you can use to test the function, clearly
specifying inputs and expected vs actual outputs:
```python
print("function call  : replace_letters('feed the geese', 'e', '_')")
print('expected output: f__d th_ g__s_')
print('actual output  :', replace_letters('feed the geese', 'e', '_'))
print('=========================')
# repeat the above lines with different inputs!
# (make sure the printed function args match the actual function call)
```

### Part 2.

Make `replacement` an optional argument whose value defaults to an underscore (`_`). Test this new version by calling it with and without this argument!


### Part 3. (harder!)

Copy-paste your new `replace_letters` function and rename the copy to `replace_letters_args`. This version of the function should require the
letters-to-be-replaced to be specified as multiple individual arguments **instead of** as a string or list (allowing both is too hard).

For example:
```python
# 'e', 'a', 'f', 'm' are all letters which will be replaced with '@'
replace_letters_args( 'feed me', 'e', 'a', 'f', 'm', '@' )
```

This might make it impossible for your function to know what the optional `replacement` argument is, i.e. it might think that when you do specify the `replacement` argument, it's actually just another one of the multiple `letters_to_replace` arguments. How can you get around this? How will you unambiguously pass a `replacement` argument to your function when you need to?

### Part 4.

Add another optional argument, `error_on_fail`, which defaults to false,
but when true will keep count of how many characters were replaced. If no
characters were replaced at all, it should print an error message "Error: no  matches!" and return an empty string, instead of the original string.

### Part 5.

What would you need to do to have the function return BOTH the changed string AND the number of characters that were replaced? (Note: I do mean RETURN those values from the function, not print them).
