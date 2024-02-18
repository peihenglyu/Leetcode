class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        thre = len(arr)/4
        num_dict = {}

        for num in arr:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
            
            if num_dict[num] > thre:
                return num

obj = Solution()
print(obj.findSpecialInteger([1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))