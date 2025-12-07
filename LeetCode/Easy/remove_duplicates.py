

# Here leetcode will check bot nums and the # Number of unique elements

# main problem is to arrange the array with unique element from left side , right side doesnot matter


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0  # Pointer for the last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Overwrite the next position with a new unique element
        print(nums)
        return i + 1  # Number of unique elements
    
obj= Solution()
nums = [0,0,1,1,1,2,2,3,3,4]

print(obj.removeDuplicates(nums))