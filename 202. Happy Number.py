class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        patterns = {}
        while True:
            if n == 1:
                return True
            if n in patterns:
                return False
            patterns[n] = 1
            sum = 0
            while n//10 != 0:
                sum += (n%10) * (n%10)
                n = n//10
            sum += (n%10) * (n%10)
            n = sum
