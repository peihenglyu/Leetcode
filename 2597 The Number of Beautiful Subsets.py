# My solution, using backtracking
class Solution:
    def beautifulSubsets(self, nums, k: int) -> int:
        
        self.beaut_count = 0
        self.num_dict = {}
        self.num_set = set()

        def iter_helper(index):
            for i in range(index, len(nums)):
                cur_num = nums[i]
                deny_num_1, deny_num_2 = cur_num + k, cur_num - k
                if deny_num_1 in self.num_dict or deny_num_2 in self.num_dict:
                    continue
                else:
                    self.beaut_count += 1

                    if cur_num not in self.num_dict:
                        self.num_dict[cur_num] = 1
                    else:
                        self.num_dict[cur_num] += 1
                    # self.num_set.add(cur_num)
                    iter_helper(i+1)
                    if self.num_dict[cur_num] > 1:
                        self.num_dict[cur_num] -= 1
                    else:
                        self.num_dict.pop(cur_num)
                    # self.num_set.remove(cur_num)

        iter_helper(0)

        return self.beaut_count


# One of the best Solution on Leetcode
# from collections import *

# class Solution:
#     def beautifulSubsets(self, nums, k: int) -> int:
        
#         # TC: O(nlogn); SC: O(n+k)
#         ans = 1
#         freq = defaultdict(Counter)

#         for x in nums:
#             freq[x % k][x] += 1

#         for fr in freq.values():
#             prevNum, curr, prev1, prev2 = -k, 1, 1, 0
#             for num in sorted(fr):
#                 skip = prev1
#                 take = (2 ** fr[num] - 1) * (prev2 if num - prevNum == k else prev1)
#                 curr = skip + take
#                 prev2, prev1 = prev1, curr
#                 prevNum = num
#             ans *= curr

#         return ans - 1

obj = Solution()
print(obj.beautifulSubsets([2,4,6], 2))
print(obj.beautifulSubsets([2,4,4,6], 2))
print(obj.beautifulSubsets([1], 1))
