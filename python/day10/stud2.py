class student:
    def set_data(self, name, mark):
        self.name = name
        self.mark = mark
    def show(self):
        print("Name :", self.name)
        print("mark :", self.mark)
s1 = student()
s2=student()
s1.set_data("jasii", 100)
s1.show()
s2.set_data("riii", 200)
s2.show()