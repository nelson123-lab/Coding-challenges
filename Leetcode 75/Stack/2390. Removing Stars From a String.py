class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == "*":
                res.pop()
            else:
                res.append(i)

        return "".join(res)

"""
The algorithm works by checking if the current character is a star or not. If it is not a star, it will be added to the results.
If it is a star the last element from the res array will be removed. It is similar to removing the character close to the star.
Time Complexity O(n)
Space Complexity O(n)
"""

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            if i == "*":
                res.pop()
            else:
                res.append(i)
        return "".join(res)

"""
Time Complexity O(n)
Space Complexity O(n) uses n extra space in the worst case scenario.
"""
