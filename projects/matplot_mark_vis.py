import matplotlib.pyplot as plt
Name = ["jasii", "ruaa", "john"]
Mark = [20, 80, 50]
plt.bar(Name, Mark)
plt.xlabel("Student")
plt.ylabel("mark")
plt.title("student mark")
plt.savefig("student_mark.png")
print("graph saved")
plt.show()
