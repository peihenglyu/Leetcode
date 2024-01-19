class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        all_time = sorted(list(set(startTime + endTime)))
        time_dict = dict(zip(all_time, range(len(all_time))))
        profit_dict = {}
        endtime_dict = {}
        end_index = {}
        last_time = 0
        for index, end in enumerate(endTime):
            if end not in end_index:
                end_index[end] = [index]
            else:
                end_index[end].append(index)

            if end not in endtime_dict:
                endtime_dict[end] = [startTime[index]]
            else:
                endtime_dict[end].append(startTime[index])
            if end > last_time:
                last_time = end

        def solver(time):
            if time == all_time[0]:
                return 0
            if time in profit_dict:
                return profit_dict[time]
            else:
                max_profit = 0
                if time in endtime_dict:
                    for index, start_time in enumerate(endtime_dict[time]):
                        cur_profit = profit[end_index[time][index]] + solver(start_time)
                        if cur_profit > max_profit:
                            max_profit = cur_profit
                
                cur_profit = solver(all_time[time_dict[time]-1])
                if cur_profit > max_profit:
                    max_profit = cur_profit
                profit_dict[time] = max_profit
                return max_profit
        
        return solver(last_time)
    
obj = Solution()
print(obj.jobScheduling([1,1,1], [2,3,4], [5,6,4]))
print(obj.jobScheduling([1,2,2,3], [2,5,3,4], [3,4,1,2]))
print(obj.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
print(obj.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
print(obj.jobScheduling([43,13,36,31,40,5,47,13,28,16,2,11], [44,22,41,41,47,13,48,35,48,26,21,39], [8,20,3,19,16,8,11,13,2,15,1,1]))