number=int(input("Enter the number of student :"))
num=1
i=0
name=[]
percent=[]
grade=[]
while num<=number:
    names=input("Enter the names of the student :")
    name.append(names)
    english=int(input("Enter marks in english :"))
    nepali=int(input("Enter marks in nepali :"))
    chemistry=int(input("Enter marks in chemistry :"))
    physicss=int(input("Enter marks in physics :"))
    computer=int(input("Enter marks in computer :"))
    totals=english+nepali+chemistry+physicss+computer
    percentage=(totals/500)*100
    percent.append(percentage)
    if(percentage>=90):
        grade.append("A+")
    elif(percentage>=80):
        grade.append("A")
    elif(percentage>=70):
        grade.append("B+")
    elif(percentage>=60):
        grade.append("B")
    elif(percentage>=50):
        grade.append("C+")
    elif(percentage>=40):
        grade.append("C-")
    num+=1
print("\n")
print("RESULT OF THE STUDENT")
while i<number:
    print(f"The result of {name[i]} is {percent[i]}% and the grade is {grade[i]}")
    i+=1

