class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        check_book = {}
        
        for i in strs:
            pharse = ''.join(sorted(i))
            if not check_book.get(pharse):
                check_book[pharse] = []
                check_book[pharse].append(i)
            else:
                check_book[pharse].append(i)
                
        return check_book.values()
        
          
            
            
