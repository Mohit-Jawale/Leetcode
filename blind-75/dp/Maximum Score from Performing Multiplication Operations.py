class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        
        @lru_cache(2000)
        def max_point(s,e,i):
            if i == len(multipliers):
                return 0
            
            op1 =  multipliers[i]*nums[s] + max_point(s+1,e,i+1)
            op2 = multipliers[i]*nums[e] + max_point(s,e-1,i+1)
            return max(op1,op2)
        
        
        return max_point(0,len(nums)-1,0)
        
        
        
