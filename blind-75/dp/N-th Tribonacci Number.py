class Solution:
    
    def __init__(self):
        self.number = {}
    
    def tribonacci(self, n: int) -> int:
     
        if n == 0:
            return 0
        if n == 1 or n==2:
            return 1
        
        if n in self.number:
            return self.number[n]
        
        
        ans = self.tribonacci(n-2) + self.tribonacci(n-1) + self.tribonacci(n-3)
        self.number[n] = ans
        return ans
        
        
