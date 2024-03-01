class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l, r = 0, len(candies)-1
        res = [0]* len(candies)
        max_cand = max(candies)
        while l<=r:
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


"""
This is a two pointer approach for solving this question
Time complexity O(n)
Space Complexity O(1) we have the option to return one result at a time but only because the question needs a list we are using it.
""""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= max_candy:
                res.append(True)
            else: res.append(False)
        return res

"""
Time complexity O(n)
Space Complexity O(1)
"""

# One Liner

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [(i + extraCandies) >= max(candies) for i in candies]

"""
This is a one liner solution with a list comprehension. Here the boolean values get automatically added to the list.
"""
