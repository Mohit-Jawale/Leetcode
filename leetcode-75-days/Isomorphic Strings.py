class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tracker_dict = {}
        
        for i in range(0,len(s)):
            if tracker_dict.get(t[i]):
                if tracker_dict[t[i]] == s[i]:
                    pass
                else:
                    return False
            else:
                tracker_dict[t[i]] = s[i]
        
        if len(set(s))== len(set(t)):
            return True
        
