num = int(input("Enter the number of student :"))
increment = 1
student_num = 1
studnet_marks = []
pass_studnet=0
fail_student=0
while increment <= num:
    print(f"Student {student_num}")
    for x in range(1):
        nep = int(input("Enter marks in nepali :"))
        eng = int(input("Enter marks in eng :"))
        mat = int(input("Enter marks in mat :"))
        science = int(input("Enter marks in science :"))
        pop = int(input("Enter marks in population :"))
        studnet_mark = [nep, eng, mat, science, pop]
        studnet_marks.append(studnet_mark)
    increment += 1
    student_num += 1

total_marks = []
for marks in studnet_marks:
    total_mark = 0
    for mark in marks:
        total_mark += mark
    percent = total_mark/5
    division = ''
    if (percent >= 90):
        division += "A+ division"
        pass_studnet+=1
    elif (percent >= 80):
        division += "A Division"
        pass_studnet+=1
    elif (percent >= 70):
        division += "B+ Division"
        pass_studnet+=1
    elif (percent >= 60):
        division += "B Division"
        pass_studnet+=1
    elif (percent >= 50):
        division += "C+ Division"
        pass_studnet+=1
    elif (percent >= 40):
        division += "C Division"
        pass_studnet+=1
    else:
        division+="Fail Try again"
        fail_student+=1
    x=1
    print("========Student Result=====")
    print(f"Student percent{percent} and his division is {division}")
print("=================Student Pass list=============")
print(pass_studnet)
print("=================Student fail list ==============")
print(fail_student)
