n= int(input("enter the number :"))
arr=[]
for i in range(n):
    num= int(input("enter the elements :"))
    arr.append(num)
print("Positive numbers in list are:")    
for i in arr:
    if i>=0:
        print(i)    