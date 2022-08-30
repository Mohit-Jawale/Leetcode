class Solution(object):
    def two_sums(self,nums,i,res):
        low=i+1
        high = len(nums)-1
        while low < high:
            sum = nums[low]+nums[high]+nums[i]
            if sum > 0:
                high-=1
            elif sum < 0 :
                low+=1
            else:
                res.append([nums[low],nums[high],nums[i]])
                high-=1
                low+=1
                while low< high and nums[low]==nums[low-1]:
                    low+=1
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        res = []
        for i in range(0,len(nums)):
            if nums[i]>0:
                break
            if i == 0 or nums[i-1]!=nums[i]:
                self.two_sums(nums,i,res)
        return res
