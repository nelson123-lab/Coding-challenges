# It's hard leetcode problem solved using dynamix programming. I was not able to solve it. The solutions is here. 

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for rod in rods:
            for diff, tallest in list(dp.items()):
                new_diff = diff + rod
                new_tallest = tallest + rod
                dp[new_diff] = max(dp.get(new_diff, 0), new_tallest)

                smaller_rod = tallest - diff + rod
                new_diff = abs(tallest- smaller_rod)
                new_tallest = max(smaller_rod, tallest)
                dp[new_diff] = max(dp.get(new_diff, 0), new_tallest)
        return dp[0]

# Reference : Explanation youtube Video
# https://youtu.be/0aUzm1vhVAQ
