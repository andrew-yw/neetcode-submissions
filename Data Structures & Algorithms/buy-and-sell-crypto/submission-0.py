class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = [0] * n #if we consider i as the selling price
        left, rght = 0, 0

        for i in range(n):
            max_profit[i] = prices[i] - min(prices[:i+1])
        
        return max(max_profit)

