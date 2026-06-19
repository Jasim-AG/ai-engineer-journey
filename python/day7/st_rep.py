marks = [80, 95, 70, 60, 90]
print("highest is", max(marks))
print("lowest is", min(marks))
print("total is", sum(marks))
print("average is", sum(marks) / len(marks))
fd = int(input("enter the mark to search: "))
if fd in marks:
    print(" mark found")
else:
    print(" mark not found")

 

