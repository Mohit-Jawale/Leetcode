class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans =[]
        count_1 = 0
        
        for num in nums:
            count_1 += 1
            count_2 = 0
            for i in nums:
                count_2 +=1
                if num + i == target and count_1 != count_2:
                    ans.append(count_1-1)
                    ans.append(count_2-1)
                    
        return set(ans)
