class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        land_count = 0
        visited = [[0]*len(grid[0]) for i in range(len(grid))]

        for m in range(len(visited)):
            for n in range(len(visited[0])):
                if visited[m][n] == 0 and grid[m][n] == '1':
                    land_count += 1
                    explore = [(m,n)]
                    visited[m][n] = 1
                    while len(explore):
                        cur_node = explore.pop()
                        cur_y = cur_node[0]
                        cur_x = cur_node[1]
                        if cur_y - 1 >= 0 and grid[cur_y - 1][cur_x] == '1' and not visited[cur_y - 1][cur_x]:
                            explore.append((cur_y - 1, cur_x))
                            visited[cur_y - 1][cur_x] = 1
                        if cur_y + 1 < len(visited) and grid[cur_y + 1][cur_x] == '1' and not visited[cur_y + 1][cur_x]:
                            explore.append((cur_y + 1, cur_x))
                            visited[cur_y + 1][cur_x] = 1
                        if cur_x - 1 >= 0 and grid[cur_y][cur_x - 1] == '1' and not visited[cur_y][cur_x - 1]:
                            explore.append((cur_y, cur_x - 1))
                            visited[cur_y][cur_x - 1] = 1
                        if cur_x + 1 < len(visited[0]) and grid[cur_y][cur_x + 1] == '1' and not visited[cur_y][cur_x + 1]:
                            explore.append((cur_y, cur_x + 1))
                            visited[cur_y][cur_x + 1] = 1
                # elif visited[m][n] == 0 and grid[m][n] == '0':
                #     visited[m][n] = 1
        
        return land_count
    
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
obj = Solution()
print(obj.numIslands(grid))