# O(m*n) O(m*n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        i, j = 0, 0
        di, dj = 0, 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        ret = []
        for _ in range(m * n):
            ret.append(matrix[i][j])
            visited[i][j] = True
            next_i, next_j = i + di, j + dj
            if 0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j]:
                i, j = next_i, next_j
            else:
                count += 1
                di, dj = directions[count % 4]
                i, j = i + di, j + dj

        return ret


# O(m*n) O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = [float("inf")] * (m * n)
        rowBegin, rowEnd, colBegin, colEnd = 0, m - 1, 0, n - 1
        count = 0

        while (rowBegin <= rowEnd and colBegin <= colEnd):
            # Travese Right
            for i in range(colBegin, colEnd + 1):
                res[count] = matrix[rowBegin][i]
                count += 1
            rowBegin += 1
            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                res[count] = matrix[i][colEnd]
                count += 1
            colEnd -= 1
            # Travese Left
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    res[count] = matrix[rowEnd][i]
                    count += 1
            rowEnd -= 1
            # Travese up
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res[count] = matrix[i][colBegin]
                    count += 1
            colBegin += 1

        return res