class Solution:
    def reverseBits(self, n: int) -> int:
        
        # bin function will convert int -> bin (string type)
        reverse = bin(n)
        # here we are choose from end i.e -1 to second character excluded.
        # the last -1 is to select intergers from behind
        reverse = reverse[-1:1:-1]
        reverse = reverse + (32-len(reverse))* '0'
        return (int(reverse,2))
        
        
