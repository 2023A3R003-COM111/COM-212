# Grades 
grades=[78, 54, 65, 87, 98, 87, 76]


for i in range(len(grades)):
    print("Grade of Student with Roll No",i+1,"is: ",end="") 
    if grades[i] >= 90:
        print("A+")
    elif grades[i] >= 80:
        print("A")
    elif grades[i] >= 70:
        print("B+")
    elif grades[i] >= 60:
        print("B")
    elif grades[i] >= 50:
        print("C+")
    elif grades[i] >= 30:
        print("C")
    else:
        print("D")
