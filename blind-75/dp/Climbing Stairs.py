class Solution:
    
    def __init__(self):
        self.step_count = {}
    
    def climbStairs(self, n: int) -> int:
        
        if n == 0 or n-1 == 0:
            return 1
        
        num_ways = 0
        
        if self.step_count.get(n):
            return  self.step_count[n]
        
        num_ways = self.climbStairs(n-1) + self.climbStairs(n-2)
   
        
        self.step_count[n] = num_ways
        return  self.step_count[n]
        
        
        
        
