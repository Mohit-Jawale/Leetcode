class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        counter = Counter(nums)
        n = set(nums)
        robs = []
        for i in n:
            robs.append(counter[i]*i)
       
        def max_point(n):
            if n == 0:
                return 0
            if n == 1:
                return robs[1]
            
            max_p = max(max_point(n-1),max_point(n-2)+robs[n])
            
            return max_p
        
        return max_point()
 
        
        
       
