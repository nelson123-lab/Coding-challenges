# Brute force approach
def max_profit(prices):
  maxProfit = 0
  for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
      curProfit = prices[j] - prices[i]
      if (curProfit > maxProfit):
        maxProfit = curProfit
  return maxProfit

"""
- Here we are going through all possible iterations and finding the maximum profit.
Time Complexity O(n2)
Space Compexity O(1)
"""

# Optimized Solution
def max_profit(prices):
  maxProfit = 0
  minPrice = prices[0]
  
  for curPrice in prices[1:]:
    maxProfit = max(maxProfit, curPrice - minPrice)
    minPrice = min(curPrice, minPrice)
  
  return maxProfit

"""
- Here the current price is compared with the minimum price each time to obtain the maxProfit.
Time Complexity O(n)
Space Compelxity O(1)
"""
