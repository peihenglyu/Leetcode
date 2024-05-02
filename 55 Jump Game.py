class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        for i in range(len(nums))[-2::-1]:
            if nums[i] == 0:
                j = i - 1
                step = 1
                pass_flag = False
                while j >= 0:
                    if nums[j] > step:
                        pass_flag = True
                        break
                    else:
                        j -= 1
                        step += 1
                if not pass_flag:
                    return False
        return True

obj = Solution()
print(obj.canJump([2,3,1,1,4]))
print(obj.canJump([3,2,1,0,4]))