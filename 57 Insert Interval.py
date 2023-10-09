class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insert_index = 0
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0]:
                insert_index = i+1
        
        
        if insert_index > 0:
            left_interval = intervals[insert_index-1]
            if left_interval[1] >= newInterval[0]:
                newInterval = [left_interval[0],max(newInterval[1],left_interval[1])]
                intervals.pop(insert_index-1)
                insert_index -= 1
            
        right_index = insert_index
        while right_index < len(intervals) and intervals[right_index][0] <= newInterval[1]:
            newInterval = [newInterval[0], max(newInterval[1],intervals[right_index][1])]
            intervals.pop(right_index)

        intervals.insert(insert_index, newInterval)

        return intervals

obj = Solution()
intervals =[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval =[4,8]
print(obj.insert(intervals,newInterval))