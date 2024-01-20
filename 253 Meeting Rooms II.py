class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)
        room_list = []
        room_count = 0
        for inter in intervals:
            start_time = inter[0]
            for i in range(len(room_list))[::-1]:
                if room_list[i] <= start_time:
                    room_list.pop(i)
                    room_count += 1

            if room_count <= 0:
                room_list.append(inter[1])
            else:
                room_count -= 1
                room_list.append(inter[1])
        
        while len(room_list):
            room_list.pop()
            room_count += 1

        return room_count



obj = Solution()
print(obj.minMeetingRooms([[0,30],[5,10],[15,20]]))
print(obj.minMeetingRooms([[7,10],[2,4]]))