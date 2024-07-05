class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initializing the first 3 values of the Tibonacci numbers
        t = [0, 1, 1]

        if n < 3:
            return t[n]
        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        return t[2]

"""
- For n > 3 we are using the tuple unpacking and the simultaneous assignment in Python to assign the values accordingly.
Time Complexity O(n)
Space Complexity O(1) since only a constant space of O(3) is used here.
"""
