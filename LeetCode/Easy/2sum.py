
def twoSum(arr, target):
    ans=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                ans.append([i, j])
                
    print(ans)
                
            

def twoSum2(arr, target):
    for i in range(len(arr)):
        composite= target - arr[1];
        
            

arr= [7, 2, 3, 2, 1, 3, 6, 5, 8, 9]
twoSum(arr, 9)


def twosum(arr, target):
    helper= {}
    for i, num in enumerate(arr):
        compliment= target - num
        if  compliment in helper:
            return [i, helper[compliment]]
        helper[num]= i
    return []
            
print(twosum([1, 24, 4, 5, 6, 8], 5))         
            
            
            
             

