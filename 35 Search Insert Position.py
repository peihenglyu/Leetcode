class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        while left <= right:
            cur = (left + right) //2
            if nums[cur] == target:
                return cur
            elif nums[cur] < target:
                left = cur + 1
            else:
                right = cur - 1
        
        return left
    
obj = Solution()
nums = [1,3,5,6]
target = 2
print(obj.searchInsert(nums,target))