def grade(mark):
    if mark>=90:
        return "A"
    elif mark>=75:
        return "B"
    elif mark>=50:   
        return "C"
    else:
        return "F"


    
mark=int(input("enter the mark: "))
k=grade(mark) 
print("Grade is ",k)   