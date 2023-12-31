class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_rain = 0
        stack = []
        for i in range(len(height)):
            if height[i] > 0 and i != 0:
                end_diff = height[i] - height[i-1]
                if end_diff > 0:
                    while end_diff > 0 and len(stack) > 0:
                        if end_diff >= stack[-1][1]:
                            end_diff -= stack[-1][1]
                            total_rain += (i - stack[-1][0] - 1) * stack[-1][1]
                            stack.pop()
                        else:
                            total_rain += (i - stack[-1][0] - 1) * end_diff
                            stack[-1] = (stack[-1][0], stack[-1][1] - end_diff)
                            end_diff = 0


            if height[i] > 0 and i != len(height)-1:
                start_diff = height[i] - height[i + 1]
                if start_diff > 0:
                    stack.append((i,start_diff))

        return total_rain

# class Solution(object):

#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left_max = 0
#         left_sup = []
#         for i in range(len(height)):
#             if height[i] > left_max:
#                 left_max = height[i]
#             left_sup.append(left_max)

#         right_max = 0
#         right_sup = []
#         for i in range(len(height))[::-1]:
#             if height[i] > right_max:
#                 right_max = height[i]
#             right_sup.insert(0, right_max)

#         sum = 0
#         for i in range(len(height)):
#             sum += min(left_sup[i], right_sup[i]) - height[i]

#         return sum
    
obj = Solution()
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))