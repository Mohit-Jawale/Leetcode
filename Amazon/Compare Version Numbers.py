class Solution(object):
    
    

        
    
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: init
        """
        
        
        #remove leading zeros
        temp1 = copy.deepcopy(version1)
        temp2 = copy.deepcopy(version2)
        temp1 = temp1.split('.')
        temp2 = temp2.split('.')
        
        length = min(len(temp1),len(temp2))
        i=0
        ans = 0
        while i < length:
            if int(temp1[i]) == int(temp2[i]):
                ans =0
            elif int(temp1[i]) > int(temp2[i]):
                ans = 1
                break
            else:
                ans = -1
                break
            i+=1
        
        if len(temp1) > len(temp2) and ans ==0:
            sum = 0
            for j in range(i,len(temp1)):
                sum = sum + int(temp1[j])
            print(sum)    
            if sum == 0:
                ans = 0
            else:
                ans = 1
        elif len(temp1) < len(temp2) and ans ==0:
            sum = 0
            for j in range(i,len(temp2)):
                sum = sum + int(temp2[j])
            print(sum)    
            if sum ==0:
                ans = 0
            else:
                ans = -1
            
        return ans
           
                
            
            
        
