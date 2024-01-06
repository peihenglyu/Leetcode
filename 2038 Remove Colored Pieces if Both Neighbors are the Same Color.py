# class Solution(object):
#     def next_step_A(self, colors, remove_c):
#         next_color_list = []
#         for i in range(1, len(colors)-1):
#             if colors[i] == colors[i-1] == colors[i+1] == remove_c:
#                 next_color_list.append(colors[:i] + colors[i+1:])
#         if not len(next_color_list):
#             return -1
        
#         result_list = []
#         for next_color in next_color_list:
#             remove_c2 = 'A' if remove_c == 'B' else 'B'
#             next_next_color_list = []
#             for i in range(1, len(colors)-1):
#                 if next_color[i] == next_color[i-1] == next_color[i+1] == remove_c2:
#                     next_next_color_list.append(colors[:i] + colors[i+1:])
        

#     def winnerOfGame(self, colors):
#         """
#         :type colors: str
#         :rtype: bool
#         """
#         result = self.next_step_A(colors, 'A')
#         return result
        

class Solution(object):

    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        a_count = 0
        b_count = 0
        for i in range(1, len(colors)-1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == 'A':
                    a_count += 1
                else:
                    b_count += 1
        
        return a_count > b_count
        