n= int(input("enter the number :"))
arr=[]
for i in range(n):
    num= int(input("enter the elements :"))
    arr.append(num)
print("odd numbers in list are:")   
for i in arr:
    if i%2!=0:
        print(i)