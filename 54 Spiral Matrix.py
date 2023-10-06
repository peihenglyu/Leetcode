class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        bound_top = -1
        bound_bottom = m
        bound_left = -1
        bound_right = n
        # [0,0]:go right, [0,1]:go left, [1,0]:go down, [1,1]:go up
        stage = [0,0]
        cur_index = [0,0]
        output = []
        while cur_index[0] > bound_top and cur_index[0] < bound_bottom and cur_index[1] > bound_left and cur_index[1] < bound_right:
            if stage == [0,0]:
                while cur_index[1] < bound_right:
                   output.append(matrix[cur_index[0]][cur_index[1]])
                   cur_index[1] += 1
                cur_index[0] += 1
                cur_index[1] -= 1
                bound_top += 1
                stage = [1,0]
            elif stage == [1,0]:
                while cur_index[0] < bound_bottom:
                   output.append(matrix[cur_index[0]][cur_index[1]])
                   cur_index[0] += 1
                cur_index[1] -= 1
                cur_index[0] -= 1
                bound_right -= 1
                stage = [0,1]
            elif stage == [0,1]:
                while cur_index[1] > bound_left:
                   output.append(matrix[cur_index[0]][cur_index[1]])
                   cur_index[1] -= 1
                cur_index[0] -= 1
                cur_index[1] += 1
                bound_bottom -= 1
                stage = [1,1]
            elif stage == [1,1]:
                while cur_index[0] > bound_top:
                   output.append(matrix[cur_index[0]][cur_index[1]])
                   cur_index[0] -= 1
                cur_index[1] += 1
                cur_index[0] += 1
                bound_left += 1
                stage = [0,0]
        return output

matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.spiralOrder(matrix))