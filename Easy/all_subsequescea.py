def getAllSubSequences(s):
    ans=[]
    n= len(s)
    for i in range(1, 1<<n):
        sub_seq=""
        for j in range(n):
            if (i & (1 << j)):
                sub_seq+=s[j]
                
        print(sub_seq)
        ans.append(sub_seq)
    return ans
    
    

getAllSubSequences("abcd")