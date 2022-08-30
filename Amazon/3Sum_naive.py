class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        i=0
        while i < len(nums):
            j=i+1
            while j< len(nums):
                if ((nums[i]+nums[j])*(-1)) in nums and (nums.index((nums[i]+nums[j])*(-1)) != i and nums.index((nums[i]+nums[j])*(-1)) != j):
                    temp_index = [nums[i],nums[j],(nums[i]+nums[j])*(-1)]
                    temp_index.sort()
                    if temp_index not in ans:
                        ans.append(temp_index)
                    
                    
                j+=1
            i+=1
        
        return  ans
