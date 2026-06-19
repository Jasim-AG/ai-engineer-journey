class Person:
    def set_Name(self, name):
        self.name = name
    def show(self):
        print("Name :", self.name)
           
        
        
class student(Person):
    def set_Mark(self, mark):
        self.mark = mark
        
    def show(self):
        super().show()
        print("Mark :", self.mark)    

s1 = student()
s2 = student()
s3 = student()

s1.set_Name("jasim")
s1.set_Mark(95)
s2.set_Name("riii")
s2.set_Mark(80)
s3.set_Name("ruaa")
s3.set_Mark(100)
s1.show()
s2.show()
s3.show()
mark = [s1.mark, s2.mark, s3.mark]
print("highest mark is ",max(mark))


        
        
