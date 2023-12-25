class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        count = 0
        left = 0
        right = 0
        num_dict = {}

        while right < len(nums):
            if count <= k:
                if nums[right] not in num_dict:
                    num_dict[nums[right]] = 1
                else:
                    return True
                count += 1
            else:
                if num_dict[nums[left]] == 1:
                    num_dict.pop(nums[left])
                else:
                    num_dict[nums[left]] -= 1
                left += 1
                if nums[right] not in num_dict:
                    num_dict[nums[right]] = 1
                else:
                    return True
            
            right += 1

        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1,2,3,1], 3))
print(obj.containsNearbyDuplicate([1,0,1,1], 1))
print(obj.containsNearbyDuplicate([1,2,3,1,2,3], 2))