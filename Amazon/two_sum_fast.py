class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping_dict = {}
        for i in range(0,len(nums)):
            mapping_dict[nums[i]]=i
           
        for i in nums:
            if mapping_dict.get(target-i) and mapping_dict[target-i]!=nums.index(i):
                    return[nums.index(i),mapping_dict[target-i]]
            
