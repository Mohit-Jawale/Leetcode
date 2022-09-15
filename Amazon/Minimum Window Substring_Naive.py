class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        min_count = 0
        ans_count = 999999999
        actual_ans= ''
        for i in range(0,len(s)):
            ans = ""
            upper_count = [0]*26
            lower_count = [0]*26
            for k in t:
                if k.isupper():
                    upper_count[ord(k)-ord('A')]+=1  
                else:    
                    lower_count[ord(k)-ord('a')]+=1  
            for j in range(i,len(s)):
                if sum(upper_count)==0 and sum(lower_count) == 0:
                    break
                elif s[j].isupper(): 
                    if upper_count[ord(s[j])-ord('A')] > 0 :
                        upper_count[ord(s[j])-ord('A')]-=1
                        ans = ans + s[j]
                        min_count +=1
                    else:
                        ans = ans + s[j]
                        min_count +=1
                else: 
                    if lower_count[ord(s[j])-ord('a')] > 0 :
                        lower_count[ord(s[j])-ord('a')]-=1
                        ans = ans + s[j]
                        min_count +=1
                    else:
                        ans = ans + s[j]
                        min_count +=1       
        
            if ans_count > min_count and sum(upper_count)==0 and sum(lower_count)== 0:
                actual_ans = ans
                ans_count = len(ans)
            min_count = 0  
            
                
        return(actual_ans)   
                
         
                
                
        
