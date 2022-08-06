class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for j in range(0,len(s)):
            temp = {}
            for i in range(j,len(s)):
                if not temp.get(s[i]):
                    temp[str(s[i])]=1
                else:
                    break   
            if len(temp.keys())>ans:
                ans = len(temp.keys())    
        return ans   
            
