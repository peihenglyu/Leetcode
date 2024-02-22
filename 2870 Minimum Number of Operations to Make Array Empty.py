class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        one_count = 0
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
                one_count += 1
            else:
                if count_dict[num] == 1:
                    one_count -= 1
                count_dict[num] += 1
        
        if one_count > 0:
            return -1
        
        step_count = 0
        for key in count_dict:
            num = count_dict[key]
            if num % 3 != 0:
                step_count += num // 3 + 1
            else:
                step_count += num // 3
        
        return step_count
