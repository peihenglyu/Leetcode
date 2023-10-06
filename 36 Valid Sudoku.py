class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        full_set = list(range(1,10))
        for i in range(9):
            # check row:
            temp_set = full_set[:]
            for j in board[i]:
                if j == ".":
                    pass
                elif int(j) in temp_set:
                    temp_set.remove(int(j))
                else:
                    print(f"row:{i}")
                    print(f"wrong with: {j}")
                    print(board[i])
                    return False
            # check column:
            temp_set = full_set[:]
            for j in [num[i] for num in board]:
                if j == ".":
                    pass
                elif int(j) in temp_set:
                    temp_set.remove(int(j))
                else:
                    print(f"coloum:{i}")
                    print(f"wrong with: {j}")
                    print([num[i] for num in board])
                    return False
            # check sub-box:
            temp_set = full_set[:]
            sub_x = int(i/3) * 3
            sub_y = i%3 * 3
            print((sub_x,sub_y))
            for j in range(3):
                for k in range(3):
                    cur_number = board[sub_x+j][sub_y+k]
                    if cur_number == ".":
                        pass
                    elif int(cur_number) in temp_set:
                        temp_set.remove(int(cur_number))
                    else:
                        print(f"sub-box:{(sub_x+j,sub_y+k)}")
                        print(f"wrong with: {cur_number}")
                        print(temp_set)
                        return False
        return True

board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
obj = Solution()

print(obj.isValidSudoku(board))


