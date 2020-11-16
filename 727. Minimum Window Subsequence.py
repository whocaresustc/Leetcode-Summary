# DFS + memo: Top down DP

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):  # the minimum substring for S[i:] and T[j:]

            if j == len(T):  # find the satisfied substring
                return i

            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)

            return memo[(i, j)]

        l, res, memo = float('inf'), '', {}

        for i, s in enumerate(S):
            if s == T[0]:  # find the first match
                j = dfs(i, 1)

                if j - i < l:  # update
                    l, res = j - i, S[i:j + 1]
        return res