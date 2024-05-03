class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
            
        result_dict = {}
        candidates = sorted(candidates)

        def iter_helper(cur_sum, cur_nums, index):
            if cur_sum == target:
                # sorted_cur_nums = sorted(cur_nums)
                answer = ' '.join([str(x) for x in cur_nums])
                if answer not in result_dict:
                    result_dict[answer] = 1
                return 0
            elif cur_sum > target:
                return 1
            
            for i in range(index, len(candidates)):
                cur_nums.append(candidates[i])
                larger_flg = iter_helper(cur_sum + candidates[i], cur_nums, i)
                cur_nums.pop()
                if larger_flg:
                    break
        
        iter_helper(0, [], 0)
        result = []
        for key in result_dict:
            result.append([int(x) for x in key.split(' ')])
        return result

obj = Solution()
print(obj.combinationSum([8,7,4,3], 11))
print(obj.combinationSum([2,3,6,7], 7))
print(obj.combinationSum([2,3,5], 8))
print(obj.combinationSum([2], 1))
            