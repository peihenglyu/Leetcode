# My first Solution, Bi-direction dictionary
# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         bi_dict = {}
#         exist_dict = {}
#         for num in nums:
#             if num not in exist_dict:
#                 if num in bi_dict:
#                     opps_list = bi_dict[num]
#                     if len(opps_list) == 1:
                        
#                         opps = opps_list[0]
#                         if opps < num:
#                             new_num = num + 1
#                         else:
#                             new_num = num - 1
                            
#                         if len(bi_dict[opps]) == 1:
#                             bi_dict[opps] = [new_num]
#                         else:
#                             bi_dict[opps].remove(num)
#                             bi_dict[opps].append(new_num)

#                         if new_num in bi_dict:
#                             bi_dict[new_num].append(opps)
#                         else:
#                             bi_dict[new_num] = [opps]
                        
#                         bi_dict.pop(num)

#                     else:
#                         if opps_list[0] < opps_list[1]:
#                             left, right = opps_list[0], opps_list[1]
#                         else:
#                             right, left = opps_list[0], opps_list[1]
                        
#                         bi_dict[left].remove(num)
#                         bi_dict[left].append(right)

#                         bi_dict[right].remove(num)
#                         bi_dict[right].append(left)
                
#                 else:
#                     if num + 1 in bi_dict:
#                         bi_dict[num + 1].append(num - 1)
#                     else:
#                         bi_dict[num + 1] = [num - 1]
                    
#                     if num - 1 in bi_dict:
#                         bi_dict[num - 1].append(num + 1)
#                     else:
#                         bi_dict[num - 1] = [num + 1]
            
#             exist_dict[num] = 1

        
#         max_count = 0
#         for key in bi_dict:
#             for opps in bi_dict[key]:
#                 diff = abs(opps - key) - 1
#                 if diff > max_count:
#                     max_count = diff
        
#         return max_count

# Secound Solution: bucket sort: Memory Limit Exceeded
class Solution:
    def longestConsecutive(self, nums):
        if not len(nums):
            return 0
        max_num = max(nums)
        min_num = min(nums)

        range_num = max_num - min_num + 1
        bucket = [0] * range_num

        for num in nums:
            bucket[num - min_num] = 1

        count = 0
        max_count = 0
        for num in bucket:
            if num == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        
        return max_count
    
obj = Solution()
print(obj.longestConsecutive([0,0,-1]))
print(obj.longestConsecutive([100,4,200,1,3,2]))
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))