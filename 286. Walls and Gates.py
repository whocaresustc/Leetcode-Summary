# O(mn) O(mn)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < m and 0 <= next_y < n and rooms[next_x][next_y] > rooms[x][y] + 1:  # not visited
                    queue.append((next_x, next_y))
                    rooms[next_x][next_y] = rooms[x][y] + 1