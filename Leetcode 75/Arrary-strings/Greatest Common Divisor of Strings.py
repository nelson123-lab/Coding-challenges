class Solution:
    """
    Recursive implementation of the Euclidean algorithm to find the greatest common divisor (GCD) of two integers a and b.
    """
    def gcd(self, a, b):
        return a if b ==0 else self.gcd(b, a%b)
      
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # IF check if the strings are equal or not when added in reverse order.
        if str1 + str2 != str2 + str1:
            return ""
        length = self.gcd(len(str1), len(str2))
        return str1[:length]


"""
Here the time complexity of the algorithm depends upon the minimum len of the string among str1 ans str2.
- Time complexity: O(log(min(len(str1), len(str2))))
- Space complexity: O(len(str1) + len(str2))
"""
