n=int(input("enter the number:"))
arr=[]
for i in range(n):
    num=int(input("enter elements of list:"))
    arr.append(num)
new=int(input("enter element to search:"))    
if new in arr:
    print(new,"element exist in list:")
else:
    print(new,"element does not exist in list")   
#  not in operator
if new  not in arr:
    print(new,"element does't exist in list:")
else:
    print(new,"element exist in list")

 
  