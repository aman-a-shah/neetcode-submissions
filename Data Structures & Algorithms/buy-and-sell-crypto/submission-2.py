class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i, num in enumerate(prices):
            max_profit = max(max(prices[i:]) - num, max_profit)

        return max_profit