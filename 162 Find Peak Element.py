class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if mid - 1 < 0:
                one_left = float('-inf')
            else:
                one_left = nums[mid-1]
            if mid + 1 >= len(nums):
                one_right = float('inf')
            else:
                one_right = nums[mid + 1]
            
            if nums[mid] > one_left and nums[mid] > one_right:
                return mid
            elif nums[mid] < one_right and nums[mid] > one_left:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

obj = Solution()
print(obj.findPeakElement([1,2,3,1]))
print(obj.findPeakElement([1,2,1,3,5,6,4]))