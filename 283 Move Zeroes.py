class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        len_nums = len(nums)
        count = 0
        while count < len_nums:
            num = nums[i]
            if num == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1
            count += 1
        
        return nums