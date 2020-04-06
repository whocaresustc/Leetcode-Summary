# Method 1: define in the main function with a self.memo and in the helper function just use it with self.memo

class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}
        return self.helper(n)

    def helper(self, n):
        if n in [0, 1]:
            return 1
        if n in self.memo:
            return self.memo[n]
        res = 0
        for i in range(1, n + 1):
            res += self.helper(i - 1) * self.helper(n - i)
        self.memo[n] = res
        return res


# Method 2: Use a helper function
class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(n, {})

    def helper(self, n, memo):
        if n in [0, 1]:
            return 1
        if n in memo:
            return memo[n]
        res = 0
        for i in range(1, n + 1):
            res += self.helper(i - 1, memo) * self.helper(n - i, memo)
        memo[n] = res
        return res