number=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]
even=[]
odd=[]
for num in number:
    for nums in num:
        if(nums%2==0):
            even.append(nums)
        else:
            odd.append(nums)
print(f"Even number list {even}")
print(f"Odd number list {odd}")