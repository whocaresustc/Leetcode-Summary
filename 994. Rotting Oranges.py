# BFS O(N) O(N)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        queue = collections.deque((i, j) for i in range(m) for j in range(n) if grid[i][j] == 2)

        d = -1
        while queue:
            d += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()  # pop out
                for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if self.is_valid(grid, next_x, next_y):
                        grid[next_x][next_y] = 2
                        queue.append((next_x, next_y))

        if any(1 in row for row in grid):
            return -1

        return max(0, d)

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 1