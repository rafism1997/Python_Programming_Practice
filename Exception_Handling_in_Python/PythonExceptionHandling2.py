# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def div(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0 , ZeroDivisionError Occured and Handled")
    else:
        print (c)
 
# Driver program to test above function
div(2.0, 3.0)
div(3.0, 3.0)

######################################################################################################

# Python program to demonstrate finally
 
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')