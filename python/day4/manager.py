marks = []
for i in range(5):
    mark = int(input("enter the marks "))
    marks.append(mark)
print("marks are ", marks)
print("highest mark is ", max(marks))
print("lowest mark is ", min(marks))
print("average mark is ", sum(marks) / len(marks))
print("second mark is ", marks[1])
print("last mark is ", marks[-1])