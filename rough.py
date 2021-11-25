number = int(input(("Enter the number of student :")))
loop = 1
i=0
list = []
name1 = []
while(loop <= number):
    name = input("Enter the name :")
    chem = int(input("Enter the marks in chem :"))
    phy = int(input("Enter the marks in physics :"))
    total = chem+phy
    percent=(total/200)*100
    list.append(percent)
    name1.append(name)
    loop += 1
while(i<number):
    print(f"{name1[i]} got {list[i]}%")
    i+=1
