marks = [10, 20, 30]
while True:
    print("1.Add marks")
    print("2.Remove marks")
    print("3.Search marks")
    print("4.Exit")
    choice = int(input("enter your choice "))
    if choice == 1:
        mark = int(input("enter the mark "))
        marks.append(mark)
        print("marks ",marks)
    elif choice == 2:
        r = int(input("enter the mark to be removed"))
        if r in marks:
            marks.remove(r)
            print("marks ", marks)
        else:
            print("mark not found")        
    elif choice == 3:
        k = int(input("enter the mark to be searched"))
        if k in marks:
            print("found")
        else:
            print("not found")
    elif choice == 4:
        print("exiting")
        break
    else:
        print("invalid choice")
