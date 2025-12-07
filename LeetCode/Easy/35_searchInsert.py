# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 




# My Solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums :
            return -1
        elif (target < nums[0]):
                return 0
        elif target > nums[len(nums)-1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i]== target:
                return i
            elif (target > nums[i]) and (target < nums[i+1]):
                return i+1
            
        return -1;


# Ai Solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)  # This line is theoretically unreachable due to earlier checks
        