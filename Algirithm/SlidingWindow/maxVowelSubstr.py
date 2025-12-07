def count_vowel(str, st, end):
    totalvowel=0
    for ch in range(st, end):
        if str[ch] in {"a", "e", "i", "o", "u"}:
            totalvowel+=1
    return totalvowel



def max_vowel_substr(s, k):
    maxvowel= count_vowel(s, 0, k)
    window= maxvowel;
    i=0 
    st= i
    end= i-1
    for j in range(k, len(s)):
        window= count_vowel(s, i+1, j+1 )
        if(window > maxvowel):
            maxvowel= window
            st= i+1
            end= j
            print(st, end)
        i+=1
    print(maxvowel)
    
    
max_vowel_substr("safikmahanamiiad", 4)




def optimized_solution(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Count vowels in first window (your initial approach)
    maxvowel = 0
    for i in range(k):
        if s[i] in vowels:
            maxvowel += 1
    window = maxvowel
    i = 0  # Your variable name
    st = 0
    end = k - 1
    # Your loop structure with j
    for j in range(k, len(s)):
        # Remove left character (arr[i]) from window
        if s[i] in vowels:
            window -= 1
        # Add right character (arr[j]) to window
        if s[j] in vowels:
            window += 1        
        # Your comparison logic
        if window > maxvowel:
            maxvowel = window
            st = i + 1  # Your index calculation
            end = j     # Your index calculation        
        i += 1  # Your increment    
    print(maxvowel)
    print(st, end)
    return maxvowel

max_vowel_substr("safikmahanamiiad", 4)