number=int(input("Enter the number of student :"))
num=1
i=1
name=[]
eng=[]
nep=[]
chem=[]
physics=[]
comp=[]
total=[]
percent=[]
while num<=number:
    names=input("Enter the names of the student :")
    name.append(names)
    english=int(input("Enter marks in english :"))
    eng.append(english)
    nepali=int(input("Enter marks in nepali :"))
    nep.append(english)
    chemistry=int(input("Enter marks in chemistry :"))
    chem.append(chemistry)
    physicss=int(input("Enter marks in physics :"))
    physics.append(physicss)
    computer=int(input("Enter marks in computer :"))
    comp.append(computer)
    totals=english+nepali+chemistry+physicss+computer
    total.append(totals)
    percentage=(totals/500)*100
    percent.append(percentage)
    num+=1

while i<=number:
    print(f"The result of {name[i]} is {percent[i]} ")
    i+=1

