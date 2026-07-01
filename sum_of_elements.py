n=int(input("enter the number:"))
arr=[]
for i in range(n):
    num=int(input("enter the elements:"))
    arr.append(num)
sum=0    
for i in arr:
    sum=sum+i
print("sum of elements in list is:",sum)    

