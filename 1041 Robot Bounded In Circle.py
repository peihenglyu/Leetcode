class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        pos_dict = {}
        position = (0,0)
        max_x = 0
        max_y = 0
        min_x = 0
        min_y = 0
        # north: 1, east: 2, south: 3, west: 4
        direction = 1
        count = 0
        while count < 4:
            last_max_x = max_x
            last_min_x = min_x
            last_max_y = max_y
            last_min_y = min_y
            for index, ins in enumerate(instructions):
                # if position not in pos_dict:
                #     pos_dict[position] = [index]
                # else:
                #     if index in pos_dict[position]:
                #         return True

                if ins == 'G':
                    if direction == 1:
                        position = (position[0], position[1]+1)
                    if direction == 2:
                        position = (position[0]+1, position[1])
                    if direction == 3:
                        position = (position[0], position[1]-1)
                    if direction == 4:
                        position = (position[0]-1, position[1])
                elif ins == 'L':
                    direction -= 1
                    if direction == 0:
                        direction = 4
                elif ins == 'R':
                    direction += 1
                    if direction == 5:
                        direction = 1

                if position[0] > max_x:
                    max_x = position[0]
                if position[0] < min_x:
                    min_x = position[0]
                if position[1] > max_y:
                    max_y = position[1]
                if position[1] < min_y:
                    min_y = position[1]
                
            if last_max_x == max_x and last_min_x == min_x and last_max_y == max_y and last_min_y == min_y:
                return True

            count += 1
            
        return False



obj = Solution()
print(obj.isRobotBounded("LRG"))
# print(obj.isRobotBounded("GGLLGG"))
# print(obj.isRobotBounded("RLLGLRRRRGGRRRGLLRRR"))