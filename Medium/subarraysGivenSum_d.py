def subarray_with_given_sum(arr, d, target):
    n= len(arr)
    ans=[]
    if n< d:
        return []
    current_sum= sum(arr[:d])
    if current_sum == target:
        ans.append(arr[:d])
        
    for i in range(d , n):
        current_sum= current_sum+ arr[i] - arr[i-d]
        if current_sum == target:
            ans.append(arr[i-d+1 : i+1])
            
    return ans
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 3
target_sum = 12
result= subarray_with_given_sum(arr, d, target_sum)
print(result)        