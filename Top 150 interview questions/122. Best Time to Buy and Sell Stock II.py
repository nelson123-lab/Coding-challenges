class Solution:
    def maxProfit(self, prices) -> int:
        left, right, total_profit = 0, 1, 0
        while right< len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                total_profit += profit
                left = right
            else:
                left = right
            right += 1
        return total_profit

"""
This is a similar to finding the max profit of stock. Here maximum profit should be obtained by continuesly buying and selling stock.
The logic is that whenever there is a profit we sell the stock and buy the stock on the same day.
We add all the profit to the total profit each time when there is a profit.
"""
