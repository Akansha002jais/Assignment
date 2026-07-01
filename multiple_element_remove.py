n= int(input("enter the number :"))
arr=[]
for i in range(n):
    num= int(input("enter the elements :"))
    arr.append(num)
print("oringinal list is:",arr)
choose=int (input("how many numbers do you want to remove from list?:"))
for i in range(choose):
    x=int(input("enter the numbers you want to remove:"))
    if x in arr:
        arr.remove(x)
print("list after removing elements:",arr)