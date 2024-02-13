class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        return next((i for i in words if i == i[::-1]), "")

"""
Time Complexity O(n)
Space Complexity O(1)
"""
