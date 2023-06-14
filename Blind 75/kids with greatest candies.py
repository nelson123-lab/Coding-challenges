class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l, r = 0, len(candies)-1
        res = [0]* len(candies)
        max_cand = max(candies)
        while l<r:
            if candies[l] + extraCandies >= max_cand:
                res[l] = True
            else:
                res[l] = False
            l += 1
            if candies[r] + extraCandies >= max_cand:
                res[r] = True
            else:
                res[r] = False
            r -=1
        return res

ans = Solution()
print(ans.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))