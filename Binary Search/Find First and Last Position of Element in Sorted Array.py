class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left , right = 0, len(nums)-1
        
        if not nums:
            return [-1,-1]
        
        # all elements are same
        if nums[left] == nums[right] and nums[left]==target:
            return [left,right]
     
        
        while left <= right:
            pivot = (left+right) // 2
            
            if nums[pivot] == target and nums[pivot-1]!= target:
                break
            elif  nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot -1
                
        if left>right:
            return [-1,-1]
        
        count = pivot
        
        for i in range(pivot,len(nums)-1):
            if nums[i+1] == target:
                count = count+1
            else:
                break
            
        return [pivot,count]
