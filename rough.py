number=int(input("Enter the number of student :"))
num=1

student_marks=[];

while num<=number:
    
    for i in range(1):
        nep = input("enter num of nepali: ")
        eng = input("enter num of english: ")
        tot_mark=[nep,eng]
        student_marks.append(tot_mark)


    num+=1


print(student_marks)
