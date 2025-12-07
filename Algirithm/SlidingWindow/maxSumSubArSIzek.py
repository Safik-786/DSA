def max_sum_subarray(arr, k):
    maxsum= sum(arr[:k])
    windowsum= maxsum
    print(maxsum)
    i=0;
    stindex= 0
    edindex= k-1
    for j in range(k, len(arr)):
        windowsum= windowsum - arr[i] + arr[j]
        print("windowsum= ", windowsum)
        if(windowsum > maxsum):
            stindex= i+1
            edindex= j
            print(stindex, edindex)
        maxsum= max(windowsum, maxsum)
        print("maxsum= ", maxsum)
        i+=1
    print(maxsum)
    print(stindex, edindex)
max_sum_subarray([1, 2, 3, 4, 2, 9, 3, 1, 3], 4)