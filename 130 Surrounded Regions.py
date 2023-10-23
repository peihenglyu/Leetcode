class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        not_flip = [[0]*len(board[0]) for i in range(len(board))]
        for i in range(0,len(not_flip)):
            for j in range(0,len(not_flip[0])):
                if board[i][j] == "O" and not not_flip[i][j] and (i==0 or i==len(not_flip)-1 or j==0 or j==len(not_flip[0])-1):
                    explore = [(i,j)]
                    while len(explore):
                        cur_node = explore.pop()
                        cur_i = cur_node[0]
                        cur_j = cur_node[1]
                        not_flip[cur_i][cur_j] = 1
                        if cur_j-1 >= 0 and board[cur_i][cur_j-1] == "O" and not not_flip[cur_i][cur_j-1]:
                            explore.append((cur_i,cur_j-1))
                            not_flip[cur_i][cur_j-1] = 1
                        if cur_j+1 < len(not_flip[0]) and board[cur_i][cur_j+1] == "O" and not not_flip[cur_i][cur_j+1]:
                            explore.append((cur_i,cur_j+1))
                            not_flip[cur_i][cur_j+1] = 1
                        if cur_i-1 >= 0 and board[cur_i-1][cur_j] == "O" and not not_flip[cur_i-1][cur_j]:
                            explore.append((cur_i-1,cur_j))
                            not_flip[cur_i-1][cur_j] = 1
                        if cur_i+1 < len(not_flip) and board[cur_i+1][cur_j] == "O" and not not_flip[cur_i+1][cur_j]:
                            explore.append((cur_i+1,cur_j))
                            not_flip[cur_i+1][cur_j] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not not_flip[i][j]:
                    board[i][j] = "X"
        
        return board

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj = Solution()
print(obj.solve(board))