class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0
        while right < len(prices):
          # we need to buy the stock on the day with minimum prices.
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

"""
Here we don't need to worry about the day when we bought the stock and the day when the stock is sold. We could easily find that if 
the question is asked to return the index of the buying the selling day. 

The main goal here is to just find the maximum profit that can be obtained.
"""
