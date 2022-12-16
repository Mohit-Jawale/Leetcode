class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s = s.lower()
        number = ""
        sign = ""
        flag = 0
        for i in range(len(s)):
            if ord(s[i])>=48 and ord(s[i])<=57:
                number+=s[i]
                flag = 1
            elif (ord(s[i])==45 or ord(s[i])==43) and flag == 0 :
                sign+=s[i]
            else:
                break    

        print(sign,number)
        INT_MIN = -pow(2,31)
        INT_MAX = pow(2,31)-1
        if number == "" or len(sign)>1:
            return 0
        ans = int(sign+number) 
        if ans< INT_MIN:
            return INT_MIN
        elif ans> INT_MAX:
            return INT_MAX
        else:
            return ans           
