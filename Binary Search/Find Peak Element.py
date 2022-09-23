class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.append(-float('inf'))
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot]> nums[pivot-1] and nums[pivot] > nums[pivot+1]:
                return pivot
            
            else:
                if nums[pivot] > nums[pivot-1]:
                    left = pivot+1
                else:
                    right = pivot-1
                    
