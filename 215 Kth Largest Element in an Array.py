# My first Solution: use binary search to maintain kth largest
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         def binary_search(cur_list, num):
#             if len(cur_list)==0:
#                 return 0
#             if len(cur_list)==1:
#                 if num < cur_list[0]:
#                     return 0
#                 else:
#                     return 1
                
#             left = 0
#             right = len(cur_list)-1
#             while right - left > 2:
#                 mid = (left + right) // 2
#                 if cur_list[mid] >= num:
#                     right = mid - 1
#                 elif cur_list[mid] < num:
#                     left = mid + 1
#             insert_i = left
#             while insert_i < len(cur_list) and cur_list[insert_i] < num:
#                 insert_i += 1

#             return insert_i
        
#         max_list = []
#         for num in nums:
#             if len(max_list) < k:
#                 max_list.insert(binary_search(max_list, num), num)
#             elif max_list[0] < num:
#                 max_list.insert(binary_search(max_list, num), num)
#                 max_list.remove(max_list[0])
        
#         return max_list[0]

# My second Solution: bucket sort
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        bucket = [0] * 20002
        for num in nums:
            bucket[num+10000] += 1
        
        count = 0
        for i in range(len(bucket))[::-1]:
            while bucket[i] > 0:
                count += 1
                bucket[i] -= 1
                if count == k:
                    return i - 10000

            
obj = Solution()
# print(sorted([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]))
print(obj.findKthLargest([3,2,1,5,6,4], 2))
# print(obj.findKthLargest([3,3,3,3,3,3,3,3,3], 8))
# print(obj.findKthLargest([7,6,5,4,3,2,1], 5))
# print(obj.findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20))