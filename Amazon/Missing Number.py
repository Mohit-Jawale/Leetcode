class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        count = 0
        for i in range(0,len(nums)):
            if (i) == nums[i]:
                pass
            else:
                return i
            
        return i+1  
