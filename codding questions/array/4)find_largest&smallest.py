arr = [1,2,-3,-4,43,2,52,653,634,3,]
sml=float('inf')
big=float('-inf')
for i in range(len(arr)):
    if arr[i]>=big:
        big = arr[i]
    if arr[i]<=sml:
        sml=arr[i]
print(big)
print(sml)