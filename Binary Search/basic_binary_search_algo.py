class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        
        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
                mid = (start+end)//2
            else:
                end = mid-1
                mid = (start+end)//2
        
        return -1
        
