mark = []
for i in range(4):
    marks = int(input("enter the marks "))
    mark.append(marks)
print("marks are ", mark)
print("first mark is ", mark[0])
print("last mark is ", mark[-1])
print("highest is ", max(mark))
print("lowest is ", min(mark))
mark.append(99)
mark.remove(50)    
print("marks ",mark)
print(30 in mark)
print(60 in mark)