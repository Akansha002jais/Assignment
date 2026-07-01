n=int(input("enter the number:"))
arr=[]
for i in range(n):
    num=int(input("enter elements of list:"))
    arr.append(num)
print("elements of list are:")     
for i in arr:
    print(i)     
# using length funtion
print("length of list:",len(arr))
#using for loop
count=0
for i in arr:
    count=count+1
print("length of list is:",count)
#using while loop
while count<len(arr):
    count=count+1
print("length of list is:",count)
      