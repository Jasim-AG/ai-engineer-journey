student = [
    {"NAME": "ruaa", "mark": 80},
    {"NAME": "jasi", "mark": 95},
    {"NAME": "riii", "mark": 70}    
]
for i in student:
    print(i["NAME"],i["mark"])
    
print("highest mark is ", max(student[0]["mark"], student[1]["mark"], student[2]["mark"]))

