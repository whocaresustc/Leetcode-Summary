class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy =   sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy,p)
            one_profit = max(one_profit,p - one_buy)
            two_buy = min(two_buy,p - one_profit)
            two_profit = max(two_profit,p - two_buy)
        return two_profit