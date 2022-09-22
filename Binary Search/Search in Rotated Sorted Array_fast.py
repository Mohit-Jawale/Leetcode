class Solution(object):
    
    
    def rotation_detection(self,nums):
        
        left = 0
        right = len(nums)-1
        
        if nums[left] < nums[right]:
            return 0
        
        while left<=right:
            pivot = (left+right) // 2
            
            if nums[pivot] > nums[pivot+1]:
                return pivot + 1
            else:
                if nums[left] <= nums[pivot]:
                    left = pivot +1
                else:
                    right = pivot -1
        
        
    
    def binary_search(self,left,right,nums,target):
        
        
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot]> target:
                right = pivot-1
            else:
                left = pivot +1
        return -1        
    
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        
        
        rotation_index = self.rotation_detection(nums)
        
        print(rotation_index)


        
        if rotation_index == 0:
            return self.binary_search(0,len(nums)-1,nums,target)
        elif target >= nums[0]  :
            return self.binary_search(0,rotation_index ,nums,target)
        elif target <nums[0]:
            return self.binary_search(rotation_index,len(nums)-1,nums,target)
