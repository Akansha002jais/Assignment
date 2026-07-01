n= int(input("enter the number :"))
arr=[]
for i in range(n):
    num= int(input("enter the elements :"))
    arr.append(num)
smallest=arr[0]
for i in arr :
    if smallest > i:
        smallest=i
print("largest element in array is:",smallest)           
