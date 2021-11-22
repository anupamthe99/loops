i=1
even=0
odd=0
num=int(input("Enter the number :"))
while i<=num:
    if (i%2==0):
        even=even+i
    else:
        odd+=i
    i=i+1

print(f"The number of even num :{even}")
print(f"The number of even num :{odd}")
