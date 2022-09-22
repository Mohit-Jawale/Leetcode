class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        search_dict = {}
        index = 0
        for i in nums:
            search_dict[i] = index
            index +=1
        
        if target in search_dict:
            return search_dict[target]
        else:
            return -1
        
