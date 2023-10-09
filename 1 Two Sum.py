class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_num:
                return [i, dict_num[diff]]
            
            dict_num[nums[i]] = i
        
        return False
    
obj = Solution()
nums = [0,4,3,0]
print(obj.twoSum(nums,0))