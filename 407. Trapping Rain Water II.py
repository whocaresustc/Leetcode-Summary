# in fact the idea is the same as the two pointer solution of Trapping Rain Water I, the difference is that in a 1-D array, there are always two pointers to choose from and we only need to compare two pointers to know when to stop, but in a 2-D array, we have more candidate pointers to choose from, so a heap can help us, and a visited set can help us exclude visited points and check when to stop.

class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        import heapq
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)  # pop out the smallest one first
            for x, y in (
            (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):  # four directions narrow the border one step by one step
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))  # update the boundary
                    visited[x][y] = 1
        return result
