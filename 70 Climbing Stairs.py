class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1, n2 = 1,2
        if n == 1:
            return n1
        if n == 2:
            return n2
        
        cur_n = 2
        while cur_n < n:
            n1, n2 = n2, n1 + n2
            cur_n += 1
        
        return n2
    
obj = Solution()
print(obj.climbStairs(1))
print(obj.climbStairs(2))
print(obj.climbStairs(3))
print(obj.climbStairs(4))
print(obj.climbStairs(5))
print(obj.climbStairs(6))
print(obj.climbStairs(7))
print(obj.climbStairs(8))