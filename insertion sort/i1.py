# insertion sort ki help se array ko sort karna .
arr=[5,2,6,4,7]

for i in range(1,len(arr)):
    key = arr[i]
    j=i-1

    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print(arr)