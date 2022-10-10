class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_money = 0
        money_robbed = {}
        def max_money_rob(n):
            
            nonlocal money_robbed
            nonlocal max_money
            
            if n==0:
                return 0
            if n == 1:
                return nums[n-1]
            if n == 2:
                return max(nums[0],nums[1])
            if n in money_robbed:
                return money_robbed[n]
          
            max_money = max(max_money_rob(n-1),(max_money_rob(n-2) + nums[n-1]))
            money_robbed[n] = max_money
            
            return(max_money)
        
        return max_money_rob(len(nums))
