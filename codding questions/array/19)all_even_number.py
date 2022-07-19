arr=[1,2,3,4,5,6,7,8,9]
arr2=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        arr2.append(arr[i])
print(arr2)