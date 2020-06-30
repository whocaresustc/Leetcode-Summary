# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [0] + [float("inf")] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)

        return min_coin[-1] if min_coin[-1] != float("inf") else -1


# Top down DFS + memo

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        return self.dfs(coins, amount, {}) if self.dfs(coins, amount, {}) != float("inf") else -1

    def dfs(self, coins, amount, memo):  # return the fewest number of coins to make up amount
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        if amount < min(coins):
            return float("inf")
        memo[amount] = min(1 + self.dfs(coins, amount - coin, memo) for coin in coins)
        return memo[amount]

