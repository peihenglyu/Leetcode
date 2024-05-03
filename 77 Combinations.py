class Solution:
    def combine(self, n: int, k: int):
        result = []
        nums = [x+1 for x in range(n)]

        def iter_helper(index, cur_nums):
            if len(cur_nums) == k:
                result.append(cur_nums[:])
                return
            for i in range(index, len(nums)):
                cur_nums.append(nums[i])
                iter_helper(i+1, cur_nums)
                cur_nums.pop()

        iter_helper(0, [])
        
        return result

obj = Solution()
print(obj.combine(4, 2))