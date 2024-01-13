class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len_n = len(nums1)
        if len_n == 1:
            return 1
        higher_track = [max(nums1[0],nums2[0]), 1]
        lower_track = [min(nums1[0],nums2[0]), 1]
        max_len = 0
        for i in range(1, len_n):
            large = max(nums1[i], nums2[i])
            small = min(nums1[i], nums2[i])

            if lower_track[0] > large:
                lower_track[1], higher_track[1] = 1, 1
            elif higher_track[0] <= small:
                lower_track[1], higher_track[1] = higher_track[1] + 1, higher_track[1] + 1
            elif small < higher_track[0] <= large and lower_track[0] <= small:
                higher_track[1] += 1
                lower_track[1] += 1
            elif higher_track[0] > large and large >= lower_track[0] > small:
                higher_track[1] = lower_track[1] + 1
                lower_track[1] = 1
            elif higher_track[0] > large and small >= lower_track[0]:
                higher_track[1] = lower_track[1] + 1
                lower_track[1] = lower_track[1] + 1
            else:
                higher_track[1] += 1
                lower_track[1] = 1
            
            higher_track[0] = large
            lower_track[0] = small
            
            if max(lower_track[1], higher_track[1]) > max_len:
                max_len = max(lower_track[1], higher_track[1])

        return max_len

obj = Solution()
print(obj.maxNonDecreasingLength([1,1], [2,2]))
print(obj.maxNonDecreasingLength([3,8], [15,2]))
print(obj.maxNonDecreasingLength([2,3,1], [1,2,1]))
print(obj.maxNonDecreasingLength([1,3,2,1], [2,2,3,4]))
print(obj.maxNonDecreasingLength([11,15,9,20,6], [15,2,11,19,16]))
print(obj.maxNonDecreasingLength([16,9,5,7,2,6], [9,5,2,5,19,12]))