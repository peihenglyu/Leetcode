# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count = 0
#         total_sum = sum(nums)
#         right_sum = []
#         left_sum = []

#         cur_sum = 0
#         for i in range(len(nums))[::-1]:
#             cur_sum += nums[i]
#             right_sum.insert(0, cur_sum)

#         cur_sum = 0
#         for i in range(len(nums)):
#             cur_sum += nums[i]
#             left_sum.append(cur_sum)

#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 left = left_sum[i-1] if i-1 >= 0 else 0
#                 right = right_sum[j+1] if j+1 < len(nums) else 0
#                 if total_sum - left - right == k:
#                     count += 1
        
#         return count

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum_dict = {}
        cur_sum = 0
        for i in range(len(nums)):

            cur_sum += nums[i]
            
            if cur_sum == k:
                count += 1

            diff = cur_sum - k
            if diff in sum_dict:
                count += sum_dict[diff]

            if cur_sum not in sum_dict:
                sum_dict[cur_sum] = 1
            else:
                sum_dict[cur_sum] += 1
        
        return count

obj = Solution()
# print(obj.subarraySum([1],0))
# print(obj.subarraySum([1,1,1],2))
print(obj.subarraySum([1,-1,0],0))
# print(obj.subarraySum([1,2,3],3))