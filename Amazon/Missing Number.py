class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict = {}
        for j in nums:
            dict[j]=1
            
        for i in range(0,len(nums)):
            if dict.get(i):
                pass
            else:
                return i
            
        return i+1  
