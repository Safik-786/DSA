arr=[12, 3, 14, 9, 1, 64, 23]                
n= len(arr)

for i in range (0, n-1):
    minm= i
    for j in range(i+1, n):
        if arr[j] < arr[minm]:
            minm= j;
    arr[i], arr[minm]= arr[minm], arr[i]
    
print(arr)




