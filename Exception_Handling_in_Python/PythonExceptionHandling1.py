#Program to handle multiple errors with one except statement

def div(i):
    if i < 4:
        #throws zerodivision error for i=3
        a=i/(i-3)

        print("Print value of a : ",a)

try:
    div(3)
    div(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")

except NameError:
    print("NameError Occurred and Handled")

    