# Top - down DP with memo O(N**2) O(N)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        self.memo = {}

        n = len(s)
        return self.dfs(s, 0, n - 1)

    def dfs(self, s, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left > right:
            return 0
        if left == right:
            return 1
        if s[left] == s[right]:
            self.memo[(left, right)] = 2 + self.dfs(s, left + 1, right - 1)
        else:
            self.memo[(left, right)] = max(self.dfs(s, left + 1, right), self.dfs(s, left, right - 1))

        return self.memo[(left, right)]


# Following Approach is dynamic programming O(N**2) O(N**2)

# First known value is DP[len(s)-1][len(s)-1]
def Longest_Palin_Subsequence(s):
    if len(s) == 0:
        return 0

    DP = [[0] * len(s) for _ in range(len(s))]

    # DP[i][j] means the length of Palindromic subsequence of substring s[i:(j+1)]
    for i in range(len(s) - 1, -1, -1):  # bottom-to-up:
        DP[i][i] = 1
        for j in range(i + 1, len(s)):  # j is larger than i
            if s[i] == s[j]:
                DP[i][j] = DP[i + 1][j - 1] + 2
            else:
                DP[i][j] = max(DP[i + 1][j], DP[i][j - 1])

    return DP[0][len(s) - 1]