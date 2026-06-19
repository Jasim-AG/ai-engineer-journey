f = open("students.txt", "w")
name = input("enter name :")
mark = input("enter mark :")
f.write("\n" + name + ":" + mark)
ch = int(input("do you want to add more? (1 for yes, 0 for no): "))
while ch == 1:
    
    name = input("enter name :")
    mark = input("enter mark :")
    f.write("\n" + name + ":" + mark)
    ch = int(input("do you want to add more? (1 for yes, 0 for no): "))
f.close()
