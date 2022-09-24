class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        whole_sum = sum(nums)
        sum_left = 0
        sum_right = whole_sum
        index = 0
        for i in nums:
            
            if sum_left == (sum_right - sum_left - i):
                return index
            else:
                sum_left += i
                
            index+=1
                
        return -1     
      
       
   
  
