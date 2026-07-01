n= int(input("enter the number :"))
arr=[]
for i in range(n):
    num= int(input("enter the elements :"))
    arr.append(num)
element=int(input("Enter the element:"))
count=0
for i in arr:
    if i==element:
        count=count+1
print("occurrence of",element,"is",count)        