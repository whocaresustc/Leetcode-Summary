# O(n) O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        lowest_price = prices[0]
        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price
            max_profit = max(max_profit, price - lowest_price)
        return max_profit