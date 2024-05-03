# Solution 1: my recursive solution, can't pass time complexity test
# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         target = float(sum(nums))/2
#         nums = sorted(nums)

#         def iter_helper(index, cur_nums, cur_sum):
#             if cur_sum > target:
#                 return -1
#             elif cur_sum == target:
#                 return 1
            
#             has_target = 0
#             for i in range(index, len(nums)):
#                 cur_nums.append(nums[i])
#                 if iter_helper(i + 1, cur_nums, cur_sum + nums[i]) == 1:
#                    has_target = True 
#                 cur_nums.pop()
#                 if has_target == -1:
#                     break
#                 elif has_target == 1:
#                     return True

#             return has_target

#         return bool(iter_helper(0, [], 0))

# Solution 2: my dp solution, passed time complexity test
# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if sum(nums) % 2 != 0:
#             return False
        
#         target = sum(nums)//2
#         nums = sorted(nums)
#         dp = [[-1 for i in range(int(target)+1)] for j in range(len(nums))]

#         def find_next_sum(index, cur_sum):
#             if dp[index][cur_sum] != -1:
#                 return dp[index][cur_sum]
#             else:
#                 if cur_sum == 0:
#                     return True
#                 elif cur_sum < 0:
#                     return False
#                 elif index < 0:
#                     return False
#                 res_take = find_next_sum(index - 1, cur_sum - nums[index])
#                 res_pass = find_next_sum(index - 1, cur_sum)
#                 dp[index][cur_sum] = res_take or res_pass
#                 return dp[index][cur_sum]
        
#         return find_next_sum(len(nums)-1, target)
    

# Solution 3: best solution on the ranking
# class Solution:
#     def canPartition(self, nums):
#         total_sum = sum(nums)
#         if total_sum & 1: return False
#         half_sum, dp = total_sum // 2, 1
#         for num in nums:
#             dp |= dp << num
#         return dp & 1 << half_sum

# Solution 4: The solution I prefer on the ranking
class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False
        target = sum(nums)//2
        
        visited = set()
        for num in nums:
            tmp = set()
            for n in visited:
                tmp.add(n + num)
            tmp.add(num)
            visited |= tmp
            if target in visited:
                return True 
        return False



obj = Solution()
print(obj.canPartition([1,5,11,5]))
print(obj.canPartition([1,2,3,5]))