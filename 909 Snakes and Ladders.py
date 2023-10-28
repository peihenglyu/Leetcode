class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def get_index(m,n,curr,step_size):
            is_odd = n%2
            curr -= 1
            next_label = curr + step_size
            next_n = (n-1) - next_label // m

            even_m = (m-1) - next_label % m
            odd_m = next_label % m
            if is_odd:
                if next_n%2==0:
                    next_m = odd_m
                else:
                    next_m = even_m
            else:
                if next_n%2==0:
                    next_m = even_m
                else:
                    next_m = odd_m
            
            if next_n < 0:
                next_n = 0
                if is_odd:
                    if next_n%2==0:
                        next_m = m-1
                    else:
                        next_m = 0
                else:
                    if next_n%2==0:
                        next_m = 0
                    else:
                        next_m = m-1
            
            return next_n, next_m

        m,n = len(board[0]), len(board)
        step_board = [float("inf")]*(m*n)
        step_board[0] = 0
        visit_stack = [1]

        while len(visit_stack):
            i = visit_stack.pop(0)
            work_index = get_index(m,n,i,0)
            work_node = board[work_index[0]][work_index[1]]
            for j in range(1,7):
                reached = get_index(m,n,i,j)
                reached_index = i+j-1
                cur_node = board[reached[0]][reached[1]]
                if reached_index >= len(step_board):
                    reached_index = len(step_board)-1
                if board[reached[0]][reached[1]] == -1:
                    if step_board[reached_index] > (step_board[i-1] + 1):
                        step_board[reached_index] = (step_board[i-1] + 1)
                        visit_stack.append(reached_index+1)
                else:
                    if step_board[board[reached[0]][reached[1]]-1] > (step_board[i-1] + 1):
                        step_board[board[reached[0]][reached[1]]-1] = (step_board[i-1] + 1)
                        visit_stack.append(board[reached[0]][reached[1]])
        
        if step_board[-1] == float("inf"):
            return -1
        return step_board[-1]
        


board = [[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]
obj = Solution()
print(obj.snakesAndLadders(board))