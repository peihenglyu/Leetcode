class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        len_nums = len(nums)
        def iter_helper(candidate_nums, choiced_nums):
            if len(choiced_nums) == len_nums:
                result.append(choiced_nums[:])
                return
            for i in range(len(candidate_nums)):
                cur_num = candidate_nums.pop(i)
                choiced_nums.append(cur_num)
                iter_helper(candidate_nums, choiced_nums)
                choiced_nums.pop()
                candidate_nums.insert(i, cur_num)

        iter_helper(nums, [])
        
        return result

obj = Solution()
print(obj.permute([1,2,3]))