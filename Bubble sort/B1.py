# bubble sort ki help se array ko sort karna .

arr=[4,2,7,5,8]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)