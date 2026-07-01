n=int(input("enter the number:"))
arr=[]
for i in range(n):
    num=int(input("enter the elements:"))
    arr.append(num)
print("original list is:",arr)    
p1=int (input("enter the first position(0-(n-1)):"))
p2=int(input("enter the second position(0-(n-1)):"))
temp=arr[p1]
arr[p1]=arr[p2]
arr[p2]=temp
print("list after swapping",arr)    
