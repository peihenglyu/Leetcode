class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cur_num = arr[0]
        cur_count = 0

        for i in range(1,len(arr)):
            if cur_count == 0:
                cur_num = arr[i]
                cur_count = 1
                continue
            if arr[i] != cur_num:
                cur_count -= 1
            else:
                cur_count += 1
        
        return cur_num

obj = Solution()
print(obj.findSpecialInteger([1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))