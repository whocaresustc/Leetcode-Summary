# O(n**2) O(n**2)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        i, j = 0, 0
        di, dj = 0, 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        val = 1
        for _ in range(n ** 2):
            matrix[i][j] = val
            val += 1
            visited[i][j] = True
            next_i, next_j = i + di, j + dj
            if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]:
                i, j = next_i, next_j
            else:
                count += 1
                di, dj = directions[count % 4]
                i, j = i + di, j + dj

        return matrix

# O(n**2) O(1)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]: # if not visited then make a right turn
                di, dj = dj, -di
            i += di
            j += dj
        return A