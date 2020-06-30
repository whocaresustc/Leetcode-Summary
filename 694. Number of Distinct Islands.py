# 695. Max Area of Island
# 200. Number of islands

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    position = []
                    self.dfs(grid, i, j, position, (0, 0))
                    islands.add(tuple(position))
        return len(islands)

    def dfs(self, grid, x, y, position, rel_position):  # relative position to the starting index
        grid[x][y] = 0
        for (delta_x, delta_y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + delta_x, y + delta_y
            if self.is_valid(grid, next_x, next_y):
                new_rel_position = (rel_position[0] + delta_x, rel_position[1] + delta_y)
                position.append(new_rel_position)
                self.dfs(grid, next_x, next_y, position, new_rel_position)

    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]