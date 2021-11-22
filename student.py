number=int((input("Enter the number :")))
i=1
names=[]
while i<=number:
    name1=input("Enter the name :")
    names.append(name1)
    i+=1
for name in names:
    print(name)
