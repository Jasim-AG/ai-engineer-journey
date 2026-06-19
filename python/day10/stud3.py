class student():
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def display(self):
        print("name :", self.name)
        print("mark :", self.mark)
s1 = student("jasii",100)
s2 = student("rii",200)
s3 = student("ruaa",300)
s1.display()
print("\n") 
s2.display()
print("\n")
s3.display()
marks = [s1.mark, s2.mark, s3.mark]
print("highest mark is :", max(marks))
