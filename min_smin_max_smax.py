# min and second min
# max and seconf max

min=0
smin=0
max=0
smax=0
nums={23,45,56,66,33,77,55}
num1=list(nums)
min=num1[0]
for i in nums:
    if max<i:
        smax=max
        max=i
    elif smax<i:
        smax=i
    if min>i:
        smin=min
        min=i
    elif smin>i:
        smin=i
        


print("Max value is: ",max)
print("Smax value is : ",smax)
print("Min value is: ",min)
print("Smin value is: ",smin)