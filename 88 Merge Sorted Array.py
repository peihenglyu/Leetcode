# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         temp_list = []
#         nums1_index = 0
#         nums2_index = 0
#         for i in range(m+n):

#             if nums2_index == n:
#                 for j in range(0, m+n-i):
#                     temp_list.append(nums1[nums1_index+j])
#                 break

#             if nums1_index == m:
#                 for j in range(0, m+n-i):
#                     temp_list.append(nums2[nums2_index+j])
#                 break

#             if nums1[nums1_index] <= nums2[nums2_index]:
#                 temp_list.append(nums1[nums1_index])
#                 nums1_index += 1
#             else:
#                 temp_list.append(nums2[nums2_index])
#                 nums2_index += 1   

#         for i in range(len(temp_list)):
#             nums1[i] = temp_list[i]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        m_count = 0
        n_count = 0
        while m_count < m or n_count < n:
            while (n_count < n and m_count == m) or (n_count < n and nums2[n_count] <= nums1[m_count]):
                result.append(nums2[n_count])
                n_count += 1
            while (m_count < m and n_count == n) or (m_count < m and nums1[m_count] <= nums2[n_count]):
                result.append(nums1[m_count])
                m_count += 1
        
        for i in range(len(result)):
            nums1[i] = result[i]

        return nums1
    
obj = Solution
print(obj.merge(obj, [1,2,3,0,0,0], 3, [2,5,6], 3))