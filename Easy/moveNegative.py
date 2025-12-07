arr = [1, -3, 5, -7, 8, -2, 10, -9]

left, right= 0, 0

while right< len(arr):
    if arr[right] < 0 :
        arr[right], arr[left]= arr[left], arr[right]
        left+=1
    right+=1
    
print(arr)
        


