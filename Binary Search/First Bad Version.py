# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        left, right = 0, n
        
        while left<=right:
            pivot = (left+right) //2
            
            if isBadVersion(pivot) == False:
                left = pivot +1
            
            else:
                if isBadVersion(pivot-1) == False:
                    return pivot
                else:
                    right = pivot -1
                
                
        
