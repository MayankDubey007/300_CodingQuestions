from attr import s


arr=[23,235,57,68,34,-4668,8,4,63,6,24,5,1,4]
s = float('inf')
b = float('-inf')
for i in range(len(arr)):
    if arr[i]>=b:
        b=arr[i]
        # print("b",b)
    if arr[i]<=s:
        s=arr[i]
        # print("s",s)
# ............start.................
# largest and Smallest
# print(b)
# print(s)
# ............end.................

# ............start.................

arr2 =[] 
for i in range(s,b+1):
    if i in arr:
        arr2.append(i)
# largest and second largest
print(arr2[len(arr2)-1])
print(arr2[len(arr2)-2])
# .............end................

# print(arr2[0])
# print(arr2[1])