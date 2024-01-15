class Solution(object):

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        jump_map = {}
        for i in range(len(stones)):
            jump_map[i] = {}
        stones_set = set(stones)
        stones_dict = dict(zip(stones, range(len(stones))))
        
        def solver(index, jump_size):
            if index == len(stones_set)-1:
                return True
            
            next_stone = stones[index] + jump_size
            if next_stone not in stones_set or jump_size == 0:
                return False
            else:
                for i in range(1):
                    next_index = stones_dict[next_stone]
                    less_step = max(0,jump_size - 1)
                    if less_step in jump_map[next_index]:
                        case_1 = jump_map[next_index][less_step]
                    else:
                        case_1 = solver(next_index, less_step)
                        jump_map[next_index][less_step] = case_1
                        if case_1:
                            break

                    if jump_size in jump_map[next_index]:
                        case_2 = jump_map[next_index][jump_size]
                    else:
                        case_2 = solver(next_index, jump_size)
                        jump_map[next_index][jump_size] = case_2
                        if case_2:
                            break

                    if jump_size + 1 in jump_map[next_index]:
                        case_3 = jump_map[next_index][jump_size + 1]
                    else:
                        case_3 = solver(next_index, jump_size + 1)
                        jump_map[next_index][jump_size + 1] = case_3
                        if case_3:
                            break

                
                return case_1 or case_2 or case_3
        

        return solver(0, 1)

obj = Solution()
print(obj.canCross([0,2]))
print(obj.canCross([0,1,3,6,10,15,21,28,36]))
print(obj.canCross([0,1,3,6,10,13,14]))
print(obj.canCross([0,1,3,5,6,8,12,17]))
print(obj.canCross([0,1,2,3,4,8,9,11]))