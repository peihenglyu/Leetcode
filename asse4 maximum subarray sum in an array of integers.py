class Solution(object):
    def max_sum_sub(self, nums):
        
        cur_sum = 0
        cur_max = float('-inf')
        for num in nums:
            cur_sum += num
            if cur_max < cur_sum:
                cur_max = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        
        return cur_max




obj = Solution()
print(obj.max_sum_sub([-2, -3, 4, -1, -2, 1, 5, -3]))