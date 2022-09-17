class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter_dict = Counter(s)
        count = 0
        index_dict = {}
        for index in s:
            index_dict[index] = count
            count+=1
               
        ans = 9999999999
        
        for i in range(0,len(s)):
            if counter_dict[s[i]] == 1:
                temp_ans = index_dict[s[i]]
                ans = min(temp_ans,ans)
                
        if ans == 9999999999:
            return -1
        else:
            return ans       
                
