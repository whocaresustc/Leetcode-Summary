# Solution 1: BFS
# O(mn) min(m, n)
from collections import deque


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    islands += 1
        return islands

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = False  # change from True to False
        while queue:
            x, y = queue.popleft()  # pop out
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y):
                    continue
                queue.append((next_x, next_y))  # if meet some conditions,add it to queue
                grid[next_x][next_y] = False

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y]  # <= not <


# Solution 2: DFS O(M*N) O(M*N)
from collections import deque


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # here is a string not a interger
                    self.dfs(grid, i, j)
                    islands += 1
        return islands

    # recursion
    def dfs(self, grid, x, y):
        grid[x][y] = '0'  # change status after visiting
        for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            next_x = x + delta_x
            next_y = y + delta_y
            if not self.is_valid(grid, next_x, next_y):
                continue
            self.dfs(grid, next_x, next_y)

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'  # <= not <

# Solution 3: Union Find with path compression and rank
# O(m * n) O(m * n)
# Union O(m*n) O(m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        self.Islands = sum(grid[i][j] == "1" for i in range(m) for j in range(n))
        parents = list(range(m * n))
        ranks = [1] * (m * n)

        def find(x):
            if x == parents[x]:
                return x
            return find(parents[x])

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return
            if ranks[root_u] < ranks[root_v]:
                root_u, root_v = root_v, root_u
            parents[root_v] = root_u
            ranks[root_u] += 1
            self.Islands -= 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    index = i * n + j
                    if i < m - 1 and grid[i + 1][j] == "1":  # go down
                        union(index, index + n)
                    if j < n - 1 and grid[i][j + 1] == "1":
                        union(index, index + 1)  # go right

        return self.Islands