# My first solution
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         output = set()

#         pos = []
#         neg = []
#         zero = []

#         for num in nums:
#             if num > 0:
#                 pos.append(num)
#             elif num< 0:
#                 neg.append(num)
#             else:
#                 zero.append(num)
        
#         if len(zero) >= 3:
#             output.add(tuple([0,0,0]))

#         pos_set = set(pos)
#         neg_set = set(neg)

#         if len(zero):
#             for i in range(len(pos)):
#                 if -1 * (pos[i]) in neg_set:
#                     output.add(tuple(sorted([pos[i], 0, -1 * (pos[i])])))

#             for i in range(len(neg)):
#                 if -1 * (neg[i]) in pos_set:
#                     output.add(tuple(sorted([neg[i], 0, -1 * (neg[i])])))

#         for i in range(len(pos)-1):
#             for j in range(i+1, len(pos)):
#                 if -1 * (pos[i] + pos[j]) in neg_set:
#                     output.add(tuple(sorted([pos[i], pos[j], -1 * (pos[i] + pos[j])])))

#         for i in range(len(neg)-1):
#             for j in range(i+1, len(neg)):
#                 if -1 * (neg[i] + neg[j]) in pos_set:
#                     output.add(tuple(sorted([neg[i], neg[j], -1 * (neg[i] + neg[j])])))

#         return output

# My second solution, backtracking, can't pass time complexity test
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         sum_dict = {}
#         def iter_helper(cur_nums, index):
#             if len(cur_nums) == 3:
#                 cur_comb = tuple(sorted(cur_nums))
#                 if sum(cur_nums) == 0 and cur_comb not in sum_dict:
#                     sum_dict[cur_comb] = 1
#             else:
#                 for i in range(index, len(nums)):
#                     cur_nums.append(nums[i])
#                     iter_helper(cur_nums, i + 1)
#                     cur_nums.pop()

#         iter_helper([], 0)
#         result = []
#         for key in sum_dict:
#             result.append(list(key))

#         return result

# My third solution with time complexity O(n^2) passed test but still performs bad
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        result_dict = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first_num = nums[i]
                second_num = nums[j]
                rest = 0 - first_num - second_num
                if rest in nums_dict:
                    rest_count = nums_dict[rest]
                    if first_num == rest:
                        rest_count -= 1
                    if second_num == rest:
                        rest_count -= 1
                    if rest_count > 0:
                        result_dict[tuple(sorted([rest, first_num, second_num]))] = 1
        
        result_list = []
        for key in result_dict:
            result_list.append(list(key))
        
        return result_list

# My forth solution taking advantage of sum to 0
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """

#         return 


obj = Solution()
print(obj.threeSum([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]))
print(obj.threeSum([0,0,0]))
print(obj.threeSum([1,1,-2]))