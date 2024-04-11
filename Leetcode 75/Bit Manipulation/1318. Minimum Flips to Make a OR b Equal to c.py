class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        while a or b or c:
            x1 = a & 1
            x2 = b & 1
            x3 = c & 1
            if (x1 | x2) != x3:
                if x1 & x2:
                    ans += 2
                else:
                    ans += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return ans

"""
time Complexity O(1)
Space complexity O(1)
"""
