# method 1: brute force, DFS with memo
# we don't need to record visited positions,
# because we can only travel from small number to large number
# time O(m*n), space O(m*n) due to recursion depth
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        self.memo = {}  # memo[(i, j)] is the maximum length of increasing path starting from (i, j)

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, self.longestPathHelper(matrix, i, j))

        return res

    def longestPathHelper(self, matrix, i, j):
        # return the max length of path starting from (i, j)
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        res = 1
        for v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            p, q = i + v[0], j + v[1]
            if p >= 0 and p < len(matrix) and q >= 0 and q < len(matrix[0]) \
                    and matrix[p][q] > matrix[i][j]:
                res = max(res, 1 + self.longestPathHelper(matrix, p, q))

        self.memo[(i, j)] = res
        return res


# DFS
class Solution(object):
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))