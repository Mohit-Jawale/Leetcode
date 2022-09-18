class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        ans = []
        prefix = 1
        suffix = 1
        ans.append(prefix)
        for i in range(0,len(nums)-1):
            prefix = nums[i]*ans[i]
            ans.append(prefix)
        
        for j in range(len(nums)-1,-1,-1):
            ans[j] = suffix * ans[j]
            suffix = suffix *nums[j]
            
        return ans  
        
