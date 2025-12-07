class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0;
        index= 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index+=1
        return index
        


        # here we have to return the index only because after storing in the array we do increament in the index+=1 line