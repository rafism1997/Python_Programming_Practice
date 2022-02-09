# Exception Handling in Python 

## Try and Except 

Try and Except statement is used to handle these errors within our code in Python. The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error in the program. Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.

How try() works? 

1. First, the try clause is executed i.e. the code between try and except clause.
2. If there is no exception, then only the try clause will run, except the clause is finished.
3. If any exception occurs, the try clause will be skipped and except clause will run.
4. If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on  to the outer try statements. If the exception is left unhandled, then the execution stops.

A try statement can have more than one except clause

### Else Clause

In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception

### Finally Keyword in Python

Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exceptions.
 

Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)
 