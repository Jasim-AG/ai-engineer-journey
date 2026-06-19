def add(a, b):
    return(a + b)
def sub(a,b):
    return(a - b)
def mul(a,b):
    return(a * b)
def div(a, b):
    if b == 0:
        return "division by zero is not allowed"
    else:
        return (a / b)
while True:

    a=int(input("enter the first number "))
    b=int(input("enter the second number "))
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.Exit")

    ch=int(input("enter the choice "))
    if ch == 1:
        print("sum is ", add(a, b))
    elif ch == 2:    
        print("difference is ", sub(a, b))
    elif ch == 3:
        print("product is ", mul(a, b))
    elif ch == 4:
        print("quotient is ", div(a, b))
    elif ch == 5:
        print("exiting")
        break    
    else:
        print("invalid choice")
