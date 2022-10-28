class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        right = len(nums)-1
        max_sum = 0
        while left < right:
            if nums[left]+nums[right]>=k:
                right-=1
            elif nums[left]+nums[right]<k:
                max_sum = max(max_sum,nums[left]+nums[right])
                left+=1
        if max_sum == 0:
            return -1
        return max_sum
