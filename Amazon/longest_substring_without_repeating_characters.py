class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
      
 
        ans=0 
        for j in range(0,len(s)):
            temp = []
            for i in range(j,len(s)):
                if s[i] not in temp:
                    temp.append(str(s[i]))
                else:
                    break   
            if len(temp)>ans:
                ans = len(temp)    
            
        return ans  
