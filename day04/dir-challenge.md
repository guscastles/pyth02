## Customising dir()

The built-in `dir(obj)` function returns a list of strings which correspond to the names of the methods that can be called on the specified object type. So `dir('a string')` returns a list of string method names, including `lower` and `isdigit`.

When this list is long, it can fill up a whole screen or more.

Make a new function which is a more compact/readable version of `dir(obj)`, called `dirs(obj)`, which uses the output of the original `dir()` but returns all the methods as a single one-line string, with a single space between each method name. (This can actually be a very short one-liner!)

Extra challenge: filter the list of methods `dirs()` returns to exclude all the less relevant internal-plumbing methods that start with a double underscore (`__`).
