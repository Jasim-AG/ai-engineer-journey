try:
    a = int(input("enter numerator number: "))
    b = int(input("enter denominator number: "))
    print(a / b)
except ZeroDivisionError:
    print("cant devide by zero")
except ValueError:
    print("enter valid number")
finally:
    print("program ended")


