class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_distance = float('inf')
        answer = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                cur_distance = abs(cur_sum - target)
                if cur_distance < min_distance:
                    min_distance = cur_distance
                    answer = cur_sum
                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
                
        
        return answer

obj = Solution()
print(obj.threeSumClosest([-1,2,1,-4], 1))
print(obj.threeSumClosest([0, 0, 0], 1))