class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_med(nums):
            num_len = len(nums)
            if num_len % 2 == 0:
                med = (nums[num_len//2] + float(nums[num_len//2-1]))/2
            else:
                med = nums[num_len//2]
            
            med_i = max(1, num_len//2)
            return med, (med_i-1, med_i)
        
        def find_med_i(nums, left, right):
            num_len = right - left
            if num_len % 2 == 0:
                med = (nums[int(left + num_len//2)] + float(nums[int(left + num_len//2-1)]))/2
            else:
                med = nums[int(left + num_len//2)]
            
            med_i = max(1, int(left + num_len//2))
            return med, (med_i-1, med_i)
        
        if not len(nums1):
            return find_med(nums2)[0]
        if not len(nums2):
            return find_med(nums1)[0]
        
        total_num = (len(nums1) + len(nums2))
        if total_num % 2 == 0:
            side_num = int(total_num / 2 - 1)
        else:
            side_num = int(total_num // 2)

        left_med, left_med_i = find_med(nums1)
        right_med, right_med_i = find_med(nums2)

        if left_med == right_med:
            return left_med

        if total_num <= 6:
            return find_med(sorted(nums1 + nums2))[0]
        
        if len(nums1) < 2:
            nums1 = sorted(nums1 + nums2[:1])
            nums2 = nums2[1:]
        elif len(nums2) < 2:
            nums2 = sorted(nums2 + nums1[:1])
            nums1 = nums1[1:]

        min_count = 0
        max_count = 0


        med_left_A, med_right_A = left_med_i[0], left_med_i[1]
        med_left_B, med_right_B = right_med_i[0], right_med_i[1]
        left_bound_A, left_bound_B = 0, 0
        right_bound_A, right_bound_B = len(nums1), len(nums2)

        while min_count < side_num or max_count < side_num:
            if (right_bound_A - left_bound_A) + (right_bound_B - left_bound_B) <= 6:
                sort_list = sorted(nums1[left_bound_A:right_bound_A] + nums2[left_bound_B:right_bound_B])
                min_rest = side_num - min_count
                max_rest = side_num - max_count
                if not max_rest:
                    sort_list = sort_list[int(min_rest):]
                else:
                    sort_list = sort_list[int(min_rest):int(-max_rest)]
                return find_med(sort_list)[0]
            
            if min_count < side_num and nums1[med_left_A] < nums2[med_left_B] and med_left_A - left_bound_A > 0:
                min_rest = side_num - min_count
                if min_rest > med_left_A - left_bound_A:
                    min_count += med_left_A - left_bound_A
                    left_bound_A = med_left_A
                else:
                    left_bound_A += min_rest
                    min_count += min_rest

                med_left_A, med_right_A = find_med_i(nums1, left_bound_A, right_bound_A)[1]

            elif min_count < side_num and nums1[med_left_A] > nums2[med_left_B] and med_left_B - left_bound_B > 0:
                min_rest = side_num - min_count
                if min_rest > med_left_B - left_bound_B:
                    min_count += med_left_B - left_bound_B
                    left_bound_B = med_left_B
                else:
                    left_bound_B += min_rest
                    min_count += min_rest

                med_left_B, med_right_B = find_med_i(nums2, left_bound_B, right_bound_B)[1]
            
            elif max_count < side_num and nums1[med_right_A] > nums2[med_right_B] and right_bound_A - med_right_A > 0:
                max_rest = side_num - max_count
                if max_rest > right_bound_A - med_right_A:
                    max_count += right_bound_A - med_right_A
                    right_bound_A = med_right_A
                else:
                    right_bound_A -= max_rest
                    max_count += max_rest

                med_left_A, med_right_A = find_med_i(nums1, left_bound_A, right_bound_A)[1]
            
            elif max_count < side_num and nums1[med_right_A] < nums2[med_right_B] and right_bound_B - med_right_B > 0:
                max_rest = side_num - max_count
                if max_rest > right_bound_B - med_right_B:
                    max_count += right_bound_B - med_right_B
                    right_bound_B = med_right_B
                else:
                    right_bound_B -= max_rest
                    max_count += max_rest


                med_left_B, med_right_B = find_med_i(nums2, left_bound_B, right_bound_B)[1]
            
            else:
                if min_count < side_num and med_left_A - left_bound_A > 0:
                    min_rest = side_num - min_count
                    if min_rest > med_left_A - left_bound_A:
                        min_count += med_left_A - left_bound_A
                        left_bound_A = med_left_A
                    else:
                        left_bound_A += min_rest
                        min_count += min_rest

                    med_left_A, med_right_A = find_med_i(nums1, left_bound_A, right_bound_A)[1]
                elif min_count < side_num and med_left_B - left_bound_B > 0:
                    min_rest = side_num - min_count
                    if min_rest > med_left_B - left_bound_B:
                        min_count += med_left_B - left_bound_B
                        left_bound_B = med_left_B
                    else:
                        left_bound_B += min_rest
                        min_count += min_rest

                    med_left_B, med_right_B = find_med_i(nums2, left_bound_B, right_bound_B)[1]
                elif max_count < side_num and right_bound_A - med_right_A > 0:
                    max_rest = side_num - max_count
                    if max_rest > right_bound_A - med_right_A:
                        max_count += right_bound_A - med_right_A
                        right_bound_A = med_right_A
                    else:
                        right_bound_A -= max_rest
                        max_count += max_rest

                    med_left_A, med_right_A = find_med_i(nums1, left_bound_A, right_bound_A)[1]
                elif max_count < side_num and right_bound_B - med_right_B > 0:
                    max_rest = side_num - max_count
                    if max_rest > right_bound_B - med_right_B:
                        max_count += right_bound_B - med_right_B
                        right_bound_B = med_right_B
                    else:
                        right_bound_B -= max_rest
                        max_count += max_rest

                    med_left_B, med_right_B = find_med_i(nums2, left_bound_B, right_bound_B)[1]




obj = Solution()
# print(obj.findMedianSortedArrays([1,3],[2]))
# print(obj.findMedianSortedArrays([1],[2,3]))
# print(obj.findMedianSortedArrays([1,2],[3,4]))
# print(obj.findMedianSortedArrays([2],[1,3,4]))
# print(obj.findMedianSortedArrays([1,2],[1,2,3]))
# print(obj.findMedianSortedArrays([1,1],[1,2]))
# print(obj.findMedianSortedArrays([0,0],[0,0]))
# print(obj.findMedianSortedArrays([1,5],[2,3,4,6]))
# print(obj.findMedianSortedArrays([1],[2,3,4,5,6,7]))
# print(obj.findMedianSortedArrays([6],[1,2,3,4,5,7,8]))
# print(obj.findMedianSortedArrays([1,5],[2,3,4,6,7]))
print(obj.findMedianSortedArrays([1,2,6],[3,4,5,7,8]))
# print(obj.findMedianSortedArrays([1,2,3,4],[-999,-988,12]))
# print(obj.findMedianSortedArrays([1,2,3,4,5,7],[5,6,7,9]))
# print(obj.findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1]))

            

