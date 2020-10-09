# Top down DP: dfs with memorization
# O(n) stack memory: O(n)
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # house 0 to n -1
        # color 0, 1, 2
        # cost[i][j]
        memo = {}
        total_house = len(costs)

        def dfs(i, color):  # the minimum cost starting with house i with color
            if (i, color) in memo:
                return memo[(i, color)]

            if i == total_house - 1:
                pass

            memo[(i, color)] = costs[i][color] + min(
                dfs(i + 1, nc) + costs[i + 1][color] for nc in range(3) if nc != color)
            return memo[(i, color)]

        return min(dfs(0, color) for color in range(3))


# Bottom up DP
def minCost(self, costs):
    for i in reversed(range(len(costs) - 1)):
        for color in range(3):
            costs[i][color] += min(costs[i + 1][nc] for nc in range(3) if nc != color)

    if len(costs) == 0:
        return 0
    return min(costs[0])  # Return the minimum in the first row.