
def right_rotate_array(arr, k):
    if not arr or k <= 0:
        return arr  # Return the original array if empty or k is non-positive
    n= len(arr)
    k= k % n
    # return arr[n-1:n-k-1:-1] + arr[0:n-k:]
    return arr[-k:] + arr[:-k]

def left_rotate_array(arr, k):
    if not arr or k<= 0:
        return arr
    n= len(arr)
    k %=n
    # return arr[-(n-k): ] + arr[: -(n-k)]
    return arr[k:] +arr[:k]

# Test cases in a while loop
test_cases = [
    ([1, 2, 3, 4, 5], 2),   # Normal case
    ([1, 2, 3, 4, 5], 5),   # Full rotation
    ([1, 2, 3, 4, 5], 0),   # No rotation
    ([1, 2, 3, 4, 5], 7),   # k > len(arr)
    ([10], 3),              # Single element array
    ([], 2),                # Empty array
]

i = 0
while i < len(test_cases):
    arr, k = test_cases[i]
    print(f"Test {i+1}: Right Rotate {arr} by {k} -> {right_rotate_array(arr, k)}")
    print(f"Test {i+1}: Left Rotate {arr} by {k} -> {left_rotate_array(arr, k)}")
    i += 1
