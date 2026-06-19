student = [
    {"NAME": "ruaa", "mark": 80},
    {"NAME": "jasi", "mark": 95},
    {"NAME": "riii", "mark": 70}    
]
find = input("enter the name to search: ")

for i in student:
    if i["NAME"] == find:
        print(i["NAME"], i["mark"])
        break
else:
    print(find + " is not found")
    