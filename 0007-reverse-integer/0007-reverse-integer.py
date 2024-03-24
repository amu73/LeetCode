
class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = 1
        rev = 0
        if x < 0:
            sign = -1
            x = x*(-1)
        
        while x>0:
            rem = x%10
            rev = rev*10 + rem
            x = x//10
         
        if not -2**31 < rev < 2**31:
            return 0
        return sign*rev
        