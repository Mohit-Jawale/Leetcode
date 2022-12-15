class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        ans = ""
        number = ""
        for i in s:
            if i != ']':
                if ord(i)>=48 and ord(i)<=57:
                    number = number + i
                else: 
                    stack.append(number)
                    number = ""    
                    stack.append(i)
            else:
                top = stack.pop()
                temp = top + i   
                while top!= '[':
                    top = stack.pop()
                    temp = top + temp
                num = stack.pop()
                temp = temp.replace('[',"").replace(']',"")
                temp = temp*int(num)
                stack.append(temp)

        return("".join(stack))       
            
