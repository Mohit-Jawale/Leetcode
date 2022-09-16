class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0,0
        
        counter_dict = Counter(t)
        
        window_count = {}
        
        required = len(counter_dict)
        
        formed = 0
        
        ans = float("inf"), None , None
        
        while r< len(s):
            char = s[r]
            window_count[char] = window_count.get(char,0) + 1
            
            if char in counter_dict and window_count[char] == counter_dict[char]:
                formed+=1
            
            while r>=l and formed == required:
                
                char = s[l]
                
                if r-l+1 < ans[0]:
                    ans = (r-l+1,l,r)
                
                window_count[char]-=1
                
                if char in counter_dict and window_count[char] < counter_dict[char]:
                    formed-=1
                l+=1    
                
            
            
            r+=1
        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]    
            
        
        
        
        
        
       
