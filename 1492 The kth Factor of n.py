class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 1
        for i in range(1,n+1):
            if n % i == 0:
                if count == k:
                    return i
                count += 1
        return -1