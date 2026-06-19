def grade(mark):
    if mark>=90:
        return "A"
    elif mark>=75:
        return "B"
    elif mark>=50:   
        return "C"
    else:
        return "F"

def result(mark):
    if mark>=40:
        return "pass"
    else:
        return "fail"

mark = int(input("enter the mark: "))
print("result :", result(mark))
print("grade : ", grade(mark))