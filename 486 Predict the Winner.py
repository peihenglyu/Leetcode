class Solution(object):

    def next_step(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        left = min(self.next_step(nums[2:]), self.next_step(nums[1:-1]))
        right = min(self.next_step(nums[1:-1]), self.next_step(nums[:-2]))

        return max(left, right)

    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.next_step(nums)
        
obj = Solution()
print(obj.predictTheWinner([1,5,233,7]))