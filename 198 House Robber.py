class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1] * (len(nums)+2)

        def helper(index):
            if index >= len(nums):
                return 0
            
            case_1_index = index + 1
            case_2_index = index + 2

            if dp[case_1_index] != -1:
                case_1_sum = dp[case_1_index]
            else:
                case_1_sum = helper(case_1_index)
            
            if dp[case_2_index] != -1:
                case_2_sum = nums[index] + dp[case_2_index]
            else:
                case_2_sum = nums[index] + helper(case_2_index)
            
            dp[index] = max(case_1_sum, case_2_sum)
            return dp[index]
        
        helper(0)
        return dp[0]




obj = Solution()
print(obj.rob([1,2,3,1]))
# print(obj.rob([2,7,9,3,1]))
print(obj.rob([2,1,1,2]))