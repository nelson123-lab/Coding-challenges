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
Space Complexity O(n)
"""

# One Liner

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [(i + extraCandies) >= max(candies) for i in candies]

"""
This is a one liner solution with a list comprehension. Here the boolean values get automatically added to the list.
"""
