def cyclicSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct_index = arr[i] - 1  # Find the correct index of the current element
        if arr[i] != arr[correct_index]:  # If not in the correct place, swap
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1  # Move to the next index only if correctly placed

# Example usage
arr = [3, 2, 5, 4, 1]
print("Before Sorting:", arr)
cyclicSort(arr)
print("After Sorting:", arr)
