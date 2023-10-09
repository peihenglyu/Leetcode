class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x: x[0])

        ranges = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if cur_start <= end:
                if end < cur_end:
                    end = cur_end
            else:
                ranges.append([start, end])
                start = cur_start
                end = cur_end

        ranges.append([start, end])
        return ranges