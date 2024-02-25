class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not len(nums):
            return [-1,-1]

        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2
            val = nums[mid]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                left = mid
                break
        
        if nums[left] != target:
            return [-1, -1]
        else:
            output = [left,left]
        
        while output[0]-1 > 0 and nums[output[0]-1] == target:
            output[0] -= 1
        while output[1]+1 < len(nums) and nums[output[1]+1] == target:
            output[1] += 1
        
        return output

obj = Solution()
print(obj.searchRange([1,1,2], 1))