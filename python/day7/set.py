marks = {10, 20, 30, 40, 50, 22}
ad = int(input("enter the mark"))
marks.add(ad)
print(marks)
find = input("enter the mark to search: ")
if find in marks:
    print("found")
else:
    print("not found")
