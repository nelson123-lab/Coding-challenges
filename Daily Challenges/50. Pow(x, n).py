class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

"""
The above solution is not an implementation of the pow function. It is just a different way of doing the pow(x, n) in python.
"""

class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

"""
This is a recursive solution where each time the x values gets multiplied by itself according to the value of n.
Time Complexity: O(log n)
Space Complexity: O(log n)
"""
