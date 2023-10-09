class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        last_num = None
        cur_range = None
        for index, num in enumerate(nums):
            if last_num == None:
                last_num = num
                cur_range = num
            elif num == last_num + 1:
                last_num = num
                
            else:
                if cur_range == last_num:
                    ranges.append(str(cur_range))
                else:
                    ranges.append(str(cur_range)+ "->" + str(last_num))
                last_num = num
                cur_range = num

            if index == len(nums)-1:
                if cur_range == last_num:
                    ranges.append(str(cur_range))
                else:
                    ranges.append(str(cur_range)+ "->" + str(last_num))
        
        return ranges
    
obj = Solution()
nums =[0,1,2,4,5,7]
print(obj.summaryRanges(nums))