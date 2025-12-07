def binary_search(arr, lb, ub, target ):
    while lb <= ub:
        mid= (lb + ub) // 2 ;
        if arr[mid] is target:
            print("Item Found at index", mid)
            return
        if target < arr[mid]:
            ub= mid-1
        else:
            lb= mid+1
    print("Item Not found..")
arr= [1, 2, 3, 4, 5, 67, 100] 
binary_search(arr, 0, len(arr)-1, 11)