class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        max_sum = -float('inf')
        for num in nums:
            cur_sum += num
            if max_sum < cur_sum:
                max_sum = cur_sum
            
            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum


            
obj = Solution()
print(obj.maxSubArray([1]))
print(obj.maxSubArray([-1]))
print(obj.maxSubArray([5,4,-1,7,8]))
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.maxSubArray([-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7]))
print(obj.maxSubArray([-5,8,-5,1,1,-3,5,5,-3,-3,6,4,-7,-4,-8,0,-1,-6]))
