# class Solution(object):
#     def maxDistToClosest(self, seats):
#         """
#         :type seats: List[int]
#         :rtype: int
#         """
#         index = 0
#         left_zero = 0
#         right_zero = 0
#         while seats[index] != 1 and index < len(seats):
#             left_zero += 1
#             index += 1
#         index = len(seats)-1
#         while seats[index] != 1 and index < len(seats):
#             right_zero += 1
#             index -= 1
        
#         if left_zero:
#             left_zero_list = [0] * (left_zero-1)
#         else:
#             left_zero_list = []
#         if right_zero:
#             right_zero_list = [0] * (right_zero-1)
#         else:
#             right_zero_list = []

#         left_zero_list.extend(seats)
#         seats = left_zero_list
#         seats.extend(right_zero_list)

#         max_count = 0
#         zero_count = 0
#         for seat in seats:
#             if seat == 0:
#                 zero_count += 1
#                 if zero_count > max_count:
#                     max_count = zero_count
#             else:
#                 zero_count = 0
        
#         return (max_count - 1) // 2 + 1

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        index = 0
        left_zero = 0
        right_zero = 0
        while seats[index] != 1 and index < len(seats):
            left_zero += 1
            index += 1
        index = len(seats)-1
        while seats[index] != 1 and index < len(seats):
            right_zero += 1
            index -= 1

        max_count = 0
        zero_count = 0
        for seat in seats[left_zero:len(seats)-right_zero]:
            if seat == 0:
                zero_count += 1
                if zero_count > max_count:
                    max_count = zero_count
            else:
                zero_count = 0
        
        mid_dist = (max_count - 1) // 2 + 1
        return max(left_zero, mid_dist, right_zero)


obj = Solution()
print(obj.maxDistToClosest([1,0,0,0,1,0,1]))
print(obj.maxDistToClosest([1,0,0,0]))
print(obj.maxDistToClosest([0,1]))