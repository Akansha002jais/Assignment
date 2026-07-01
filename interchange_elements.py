n=int(input("enter the number:"))
arr=[]
for i in range(n):
    num=int(input("enter the element:"))
    arr.append(num)
print("elements of array without any changes:")
for i in arr:
    print(i)
temp=arr[0]
arr[0]=arr[n-1]
arr[n-1]=temp
print("After interchange of elements:")
for i in arr:
    print(i)