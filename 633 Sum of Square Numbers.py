import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(0, math.ceil(math.sqrt(c))):
            if math.sqrt(c - i**2).is_integer():
                return True
        
        return False