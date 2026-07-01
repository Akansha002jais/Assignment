n= int(input("enter the number:"))
arr=[]
for i in range(n):
    num= int(input("enter the elements:"))
    arr.append(num)
mul=1
for i in arr:
    mul= mul*i
print("multiplication of array is:",mul)    
new= int(input("enter the number:"))
rem=mul%new
print("remainder of multiplication of array divided by n is:",rem)   
