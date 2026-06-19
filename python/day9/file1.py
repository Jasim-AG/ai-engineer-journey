f = open("test.txt", "w")
f.write("hello jasii")
f.close()
print("data written")
f1 = open("test1.txt", "w")
f1.write("hai jasiii")
f1.close()
f1 = open("test1.txt", "r")
text = f1.read()
print(text)
f1.close()
f = open("test.txt", "a")
f.write("\nwelcome to python world")
f.close()



