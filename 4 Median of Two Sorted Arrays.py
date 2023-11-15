class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_n = len(nums1) + len(nums2)
        if total_n %2 == 0:
            left_rest = total_n/2 - 1
            right_rest = total_n/2 - 1
        else:
            left_rest = total_n//2
            right_rest = total_n//2
        

        while left_rest and right_rest:
            small_left = 0
            small_right = 0
            large_left = 0
            large_right = 0
            n1_half = (n1_max - n1_min)//2
            n2_half = (n2_max - n2_min)//2
            print(f'n1_half:{n1_half}')
            print(f'n2_half:{n2_half}')
            n1_med = nums1[n1_half]
            n2_med = nums2[n2_half]
            print(f'n1_med:{n1_med}')
            print(f'n2_med:{n2_med}')
            if n1_med < n2_med:
                left_cut = min(n1_half, left_rest)
                n1_min = left_cut
                right_cut = min(n2_half, right_rest)
                n2_max -= right_cut
            else:
                left_cut = min(n2_half, left_rest)
                n2_min = left_cut
                right_cut = min(n1_half, right_rest)
                n1_max -= right_cut
        
        if total_n %2 == 0:
            return nums1[n1_min]
        else:
        return 

