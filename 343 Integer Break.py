class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        
        if n == 3:
            return 2

        rest = n % 3
        if rest == 0:
            return (3**(n//3))
        
        if rest == 1:
            return (3**(n//3-1))*4
        
        if rest == 2:
            return (3**(n//3))*2

obj = Solution()
print(obj.integerBreak(10))