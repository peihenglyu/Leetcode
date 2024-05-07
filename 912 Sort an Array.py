# quick sort, can't pass time complexity test
# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         def partition(left, right):
#             if left >= right:
#                 return
#             pivot = nums[right]
#             first_larger = left
#             for i in range(left, right):
#                 if nums[i] < pivot:
#                     temp = nums[i]
#                     nums[i] = nums[first_larger]
#                     nums[first_larger] = temp
#                     first_larger += 1
        
#             temp = nums[first_larger]
#             nums[first_larger] = nums[right]
#             nums[right] = temp

#             partition(left, first_larger - 1)
#             partition(first_larger + 1, right)

#         partition(0, len(nums)-1)
        
#         return nums

# merge sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(left, right):
            if right - left == 0:
                return [nums[left]]
            if right - left >= 1:
                # partition
                mid = (left + right) // 2
                left_nums = merge_sort(left, mid)
                right_nums = merge_sort(mid + 1, right)

                # merge and sort
                index_left = 0
                index_right = 0
                cur_nums = []
                while index_left < len(left_nums) or index_right < len(right_nums):
                    if index_left == len(left_nums):
                        while index_right < len(right_nums):
                            cur_nums.append(right_nums[index_right])
                            index_right += 1
                    elif index_right == len(right_nums):
                        while index_left < len(left_nums):
                            cur_nums.append(left_nums[index_left])
                            index_left += 1
                    else:
                        left_num = left_nums[index_left]
                        right_num = right_nums[index_right]
                        if left_num > right_num:
                            cur_nums.append(right_num)
                            index_right += 1
                        else:
                            cur_nums.append(left_num)
                            index_left += 1
                return cur_nums
        return merge_sort(0, len(nums)-1)

obj = Solution()
print(obj.sortArray([5,2,3,1]))
print(obj.sortArray([5,1,1,2,0,0]))