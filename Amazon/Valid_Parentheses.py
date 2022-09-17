class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets_stack = []
        mapping_dict = {}
        count=0
        for i in ['(','[','{',')',']','}']:
            mapping_dict[i]= count*2
            count +=1    
        for bracket in s:
            if bracket in ['(','[',"{"]:
                open_brackets_stack.append(bracket)
            else:
                if open_brackets_stack :
                    top = open_brackets_stack.pop()
                else:
                    open_brackets_stack.append(bracket)
                    break
                if not mapping_dict[top] == mapping_dict[bracket]-6:
                    return False
                
        if open_brackets_stack:
            return False
        else:
            return True
