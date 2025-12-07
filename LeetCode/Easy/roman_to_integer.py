class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_rule= {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i=0;
        j=1;
        ans=0;
        while(j < len(s)):
            if roman_rule.get(s[i]) < roman_rule.get(s[j]):
                ans= ans-roman_rule.get(s[i])
            else:
                ans= ans+roman_rule.get(s[i])
            i+=1
            j+=1
        ans+= roman_rule.get(s[i])
        print(ans)
    
obj = Solution()
obj.romanToInt("MCMXCIV")
    
                
    