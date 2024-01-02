class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        left = len(nums)-2
        right = len(nums)-1


        if nums[right] > nums[left]:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            return nums
        else:
            while nums[left] >= nums[right]:
                if left == 0:
                    right = len(nums)-1
                    while left < right:
                        temp = nums[right]
                        nums[right] = nums[left]
                        nums[left] = temp
                        left += 1
                        right -= 1
                    return nums

                left -= 1
                right -= 1
                    

            larger = float('inf')
            larger_i = -1
            while right < len(nums):
                if nums[right] - nums[left] > 0 and nums[right] - nums[left] <= larger - nums[left]:
                    larger = nums[right]
                    larger_i = right
                right += 1
            
            temp = nums[larger_i]
            nums[larger_i] = nums[left]
            nums[left] = temp

            left += 1
            right = len(nums)-1
            while left < right:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
                right -= 1
            
            return nums


obj = Solution()
print(obj.nextPermutation([1,1]))
print(obj.nextPermutation([1,2]))
print(obj.nextPermutation([2,1]))
print(obj.nextPermutation([1,5,1]))
print(obj.nextPermutation([1,2,3]))
print(obj.nextPermutation([3,2,1]))
print(obj.nextPermutation([1,3,2]))
print(obj.nextPermutation([1,2,3,4]))
print(obj.nextPermutation([4,3,2,1]))
print(obj.nextPermutation([4,2,1,3]))
print(obj.nextPermutation([4,3,1,2]))
print(obj.nextPermutation([4,2,5,3,1]))
print(obj.nextPermutation([4,2,5,4,4]))