arr=[5,3,8,1,9]

#Traversing
for i in arr:
    print(i, end = " ")

#inserting
n=int(input("\nGive the number to be inserted: "))
i=int(input("\nGive the index: "))
arr=arr[:i]+[n]+arr[i:]
print("\nArray after inserting:",arr)

#deleting
m=int(input("\nGive index to be deleted: "))
arr=arr[:m]+arr[m+1:]
print("\nArray after deleting: ",arr)

#searching
l=int(input("\nGive element to search: "))
for j in range(len(arr)):
    if arr[j]==l:
        print("\nThe element is found at index ",j)

#updating
x=int(input("\nGive the number to be Updated: "))
y=int(input("\nGive the index: "))
arr[y]=x
print("\nArray after updating: ",arr)