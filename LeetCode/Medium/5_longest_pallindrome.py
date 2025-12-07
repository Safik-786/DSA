class Solution(object):
    def is_pallindrome(self, s):
        s1= s
        return s1 == s[::-1]
    # Bruteforce Solution
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # i=0
        lps=0
        arr=[]
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                if self.is_pallindrome(s[i: j]):
                    lps= max(lps, len(s[i:j ]))
        print(lps)
        
    # Concepts: choose every  items from 1st index chech from left and right in both even mode and odd mode
    def optimized_solution(self, s):
        lps=0
        
        for i in range(1, len(s)):
            left=i 
            right=i
            # Check the Odd pallindrome
            while( left>=0 and right< len(s) and (s[left] == s[right])):
                left-=1
                right+= 1 
            lps= max(len(s[(left+1) : right]), lps)
                
            right= i
            left= i-1
            while( left >= 0 and right< len(s) and (s[left]== s[right]) ):
                left -=1
                right+=1
            lps= max(len(s[(left+1) : right]), lps)

            
        
obj= Solution()
obj.longestPalindrome("abbabbad")            
            
        
# print(Solution.is_pallindrome(""))

# arr= list(range(5,-1, -1))
# print(arr)


