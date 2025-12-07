class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        arbitary= strs[0]
        ans=""
        for i in range(len(arbitary)):
            current_char= arbitary[i]
            for singleStr in strs[1:]:
                if singleStr[i] != current_char:
                    return ans
            ans+= current_char
        print("ans= ", ans)
        return ans
    
    def longestCommonPrefixOptimal(self, strs):
        sorted_arr= sorted(strs)
        ans= ""
        for i in range(len(sorted_arr[0])):
            if sorted_arr[0][i] != sorted_arr[len(sorted_arr)-1][i]:
                return ans
            ans+= sorted_arr[0][i]
        print(ans)
        return ans
                    
obj= Solution()
# print(obj.longestCommonPrefix(["aa", "ab"]))
print(obj.longestCommonPrefixOptimal(["flower", 'Florida', "Flow", "Flown"]))