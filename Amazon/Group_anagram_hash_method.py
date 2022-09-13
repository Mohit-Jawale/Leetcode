class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        check_book = {}
        ans = collections.defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] +=1
            ans[tuple(count)].append(i)
        return ans.values()   
            
        
          
            
            
