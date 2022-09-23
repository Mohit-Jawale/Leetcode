class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        #if there is only one element in the array
        if len(nums) ==1:
            return nums[0]
        
        # if the array is already sorted
        if nums[left] < nums[right]:
            return nums[0]
    
        #rotation function
        while left <= right:
            pivot = (left+right)//2
            print(pivot)
            if nums[pivot] > nums[pivot+1]:
                  break
            else:
                #here there is equal bcz comparing with self
                if nums[pivot] >=nums[left]:
                    left = pivot+1
                else:
                    right = pivot-1
                    
                
        return nums[pivot+1]
