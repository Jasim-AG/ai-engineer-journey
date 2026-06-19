n = int(input("enter the 1st number "))
m = int(input("enter the 2nd number "))
while True:
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    choice = int(input("enter your choice "))
    if choice == 1:
        print(n + m)
    elif choice == 2:
        print(n - m)
    elif choice == 3:
        print(n * m)
    elif choice == 4:
        if m != 0:
            print(n / m)
        else:
            print("cannot divide by zero")
    elif choice == 5:
        break
    else:
        print("invalid choice")
    