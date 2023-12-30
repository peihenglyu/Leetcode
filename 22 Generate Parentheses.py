# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         pa_list = ["("]
#         count = 1
#         while count < n*2:
#             new_list = []
#             for pa in pa_list:
#                 left_count = pa.count("(")
#                 right_count = pa.count(")")
#                 if right_count < left_count:
#                     new_list.append(pa + ")")
#                 if left_count < n:
#                     new_list.append(pa + "(")
#             pa_list = new_list
#             count += 1

#         return pa_list
    
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pa_list = []
        def genereat_pa(cur, left_count, right_count):
            if len(cur) == n*2:
                pa_list.append(cur)
            
            if left_count < n:
                genereat_pa(cur + "(", left_count + 1, right_count)

            if right_count < left_count:
                genereat_pa(cur + ")", left_count, right_count + 1)
        
        genereat_pa("", 0, 0)
        return pa_list

obj = Solution()
print(obj.generateParenthesis(1))
print(obj.generateParenthesis(3))
print(obj.generateParenthesis(7))