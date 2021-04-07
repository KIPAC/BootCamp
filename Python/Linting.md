# Using linters for code checking


I've put some example code in the [xipe](xipe) sub-directory.

I wrote two python classes, and then used them to print "Hello World".   One class is clean and simple, they other is less so.

Running the code that uses the two different classes get the same results.

```console
(kipac) ada$ xipe/worstCodeEver.py
Hello World
(kipac) ada$ xipe/better_code.py
Hello World
```

You can see the code [worstCodeEver](./xipe/worstCodeEver.py) and [better_code](./xipe/better_code.py)

Ok, lets run the 'pylint' linter on the code.

```console
(kipac) ada$ pylint xipe/better_code.py
...
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Looks good.  Now we try the other one.


```console
(kipac) ada$ pylint xipe/worstCodeEver.py
...
--------------------------------------------------------------------
Your code has been rated at -8.38/10 (previous run: -8.38/10, +0.00)
```

Ok, some of the messages are about things like whitespace, and our choice of variable names.

If we decide we don't want to care about those for now, we can use a different pylint configuration file that is somewhat gentler and
won't complain about whitespace and variables names.



```console
(kipac) ada$ pylint --rcfile .pylintrc_soft xipe/worstCodeEver.py
...
--------------------------------------------------------------------
Your code has been rated at -2.88/10 (previous run: -8.38/10, +5.50)
```

Ok, still a lot of error messages, let's have a look.


```console
(kipac) ada$ pylint --rcfile .pylintrc_soft xipe/worstCodeEver.py
************* Module worstCodeEver
xipe/worstCodeEver.py:81:0: C0305: Trailing newlines (trailing-newlines)
xipe/worstCodeEver.py:1:0: C0114: Missing module docstring (missing-module-docstring)
xipe/worstCodeEver.py:4:0: W0401: Wildcard import glob (wildcard-import)
xipe/worstCodeEver.py:5:0: C0115: Missing class docstring (missing-class-docstring)
xipe/worstCodeEver.py:5:0: R0205: Class 'WorstClassEver' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
xipe/worstCodeEver.py:6:4: E0101: Explicit return in __init__ (return-in-init)
xipe/worstCodeEver.py:8:71: E1101: Instance of 'WorstClassEver' has no 'missing' member (no-member)
xipe/worstCodeEver.py:9:12: C0415: Import outside toplevel (copy) (import-outside-toplevel)
xipe/worstCodeEver.py:13:8: W0702: No exception type(s) specified (bare-except)
xipe/worstCodeEver.py:12:13: C0321: More than one statement on a single line (multiple-statements)
xipe/worstCodeEver.py:12:71: E1101: Instance of 'WorstClassEver' has no 'missingFunc' member (no-member)
xipe/worstCodeEver.py:13:16: C0321: More than one statement on a single line (multiple-statements)
xipe/worstCodeEver.py:14:8: R1705: Unnecessary "elif" after "return" (no-else-return)
xipe/worstCodeEver.py:14:8: W0125: Using a conditional statement with a constant value (using-constant-test)
xipe/worstCodeEver.py:14:18: C0321: More than one statement on a single line (multiple-statements)
xipe/worstCodeEver.py:15:8: W0125: Using a conditional statement with a constant value (using-constant-test)
xipe/worstCodeEver.py:17:12: W0702: No exception type(s) specified (bare-except)
xipe/worstCodeEver.py:16:17: C0321: More than one statement on a single line (multiple-statements)
xipe/worstCodeEver.py:17:20: C0321: More than one statement on a single line (multiple-statements)
xipe/worstCodeEver.py:6:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
xipe/worstCodeEver.py:9:12: W0611: Unused import copy (unused-import)
xipe/worstCodeEver.py:10:8: W0612: Unused variable 'msg' (unused-variable)
xipe/worstCodeEver.py:21:4: R0913: Too many arguments (8/5) (too-many-arguments)
xipe/worstCodeEver.py:21:38: W0613: Unused argument 'arg1' (unused-argument)
...
```

If you haven't played around with a linter before, it is probably worth spending some time and making sure you
understand the reason behind the various error messages.


### flake8

flake8 is similar to pylint.   It seems to get a bit more use in automated code management tools, but it doesn't have the nice summary and the score to encourage you to do better.

```console
flake8 xipe/worstCodeEver.py
xipe/worstCodeEver.py:2:1: F401 'argparse' imported but unused
xipe/worstCodeEver.py:3:1: F401 'os' imported but unused
xipe/worstCodeEver.py:4:1: F403 'from glob import *' used; unable to detect undefined names
xipe/worstCodeEver.py:5:1: E302 expected 2 blank lines, found 0
xipe/worstCodeEver.py:8:80: E501 line too long (84 > 79 characters)
xipe/worstCodeEver.py:9:13: F401 'copy' imported but unused
xipe/worstCodeEver.py:9:24: E261 at least two spaces before inline comment
xipe/worstCodeEver.py:9:24: E262 inline comment should start with '# '
xipe/worstCodeEver.py:9:40: W291 trailing whitespace
...
```

One thing that you will notice is that there are a lot of messages about formatting.  There are a few different tools that will automatically format
code to standards.   One example is `black`

```console
cp xipe/worstCodeEver.py xipe/worstCodeEver_copy.py     
black xipe/worstCodeEver_copy.py
pylint xipe/worstCodeEver_copy.py
...
--------------------------------------------------------------------
Your code has been rated at -6.00/10 (previous run: -6.00/10, +0.00)
```

Ok, it is still terrible, but at least the formatting is ok.
