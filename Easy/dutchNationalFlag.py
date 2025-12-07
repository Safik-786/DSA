def sort_colors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:  # Swap 0s to the left
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:  # Keep 1s in the middle
            mid += 1
        else:  # Swap 2s to the right
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [2, 0, 1, 2, 1, 0, 1, 2, 0]
sort_colors(arr)
print(arr)  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]
