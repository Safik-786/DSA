class Solution(object):
    @classmethod
    def isValid(cls, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            new_s = s.replace("()", "").replace("[]", "").replace("{}", "")
            if new_s == s:  # No more replacements possible
                break
            s = new_s
        return len(s) == 0
    @classmethod
    def isValidOptimal(cls, s):
        bracket_map= {")":"(", "]":"[", "}":"{"}
        stack=[]
        for char in s:
            if char in bracket_map:
                    top= stack.pop() if stack else "#"    #if stack else "#" , this line when initially we got the closing bracket but here stack is empty here top value is  "#"
                    if  bracket_map[char] != top:
                        return False
            else:
                stack.append(char)
        return len(stack) == 0
                    
s = "(]"


print(Solution.isValidOptimal(s))