n= int(input("enter the number :"))
arr=[]
for i in range(n):
    num= int(input("enter the elements :"))
    arr.append(num)
largest=arr[0]
Slargest=arr[1]
for i in arr :
    if largest < i:
        largest=i
print("largest element in array is:",largest) 
for i in arr:
    if Slargest > largest and Slargest < i:
        Slargest=i
print("Slargest no. is:",Slargest)                 
