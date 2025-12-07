# Longest Substring without repeating character

def longest_substr_wrc(s):
    max_len_unique_substr= 1
    arr=[]     # for the optimization use set instead of the list
    left=0
    arr.append(s[left])
    for right in range(1,len(s)):
        if not s[right] in arr:
            arr.append(s[right])
            max_len_unique_substr= max(max_len_unique_substr, len(arr))
        else:
            arr.remove(s[left])
            left+=1
    print(max_len_unique_substr)
    
longest_substr_wrc("ssafiksaafiksafqwertyuiop")