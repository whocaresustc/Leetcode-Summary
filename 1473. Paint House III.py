# check 256. Paint House

# house is from 0 to m - 1
# color is from 1 to n

# https://leetcode.com/problems/paint-house-iii/discuss/674313/Simple-Python-explanation-and-why-I-prefer-top-down-DP-to-bottom-up

# Top down DP: dfs with memorization
# Time: O(target * m * n * n)  Space: O(target * m * n)

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        def dfs(i, t, p):  # minimum cost to paint house from i to m - 1 with t unique neighboorhoods remaining when color[i -1] = p
            key = (i, t, p)

            if i == m or t < 0 or m - i < t:
                return 0 if t == 0 and i == m else float("inf")

            if key not in dp:
                if houses[i] == 0:
                    dp[key] = min(dfs(i + 1, t - (p != nc), nc) + cost[i][nc - 1] for nc in range(1, n + 1))

                else:
                    dp[key] = dfs(i + 1, t - (p != houses[i]), houses[i])

            return dp[key]

        dp = {}
        ans = dfs(0, target, -1)

        return ans if ans < float("inf") else -1




