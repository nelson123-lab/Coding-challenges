class Solution(object):
    def maxProfit(self, prices):
        """
        Using two pointer approach but in a different way. 
        Here the order is important it determines the order in which the stocks are priced.
        """
        l, r, maxP = 0, 1, 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
