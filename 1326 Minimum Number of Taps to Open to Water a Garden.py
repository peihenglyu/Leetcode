class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        index = 0
        count = 0
        while index < n:
            max_range = 0
            range_i = -1
            for i in range(len(ranges)):
                if ranges[i]:
                    if abs(i - index) <= ranges[i]:
                        if i + ranges[i] > range_i + max_range:
                            max_range = ranges[i]
                            range_i = i
            
            if range_i == -1 or index == range_i + max_range:
                return -1
            else:
                index = range_i + max_range
                count += 1
        
        return count
    
obj = Solution()
print(obj.minTaps(7, [1,2,1,0,2,1,0,1]))
print(obj.minTaps(8, [4,0,0,0,4,0,0,0,4]))
print(obj.minTaps(5, [4,3,1,2,0,0]))
print(obj.minTaps(5, [3,0,1,1,0,0]))