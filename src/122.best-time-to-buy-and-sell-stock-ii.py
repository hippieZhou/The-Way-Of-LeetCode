class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = profit + prices[i] - prices[i-1]
        return profit

    def maxProfit(self, prices: list) -> int:
        return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))
