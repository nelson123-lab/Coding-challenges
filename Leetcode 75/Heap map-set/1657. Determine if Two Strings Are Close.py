# Approach 1
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2): return False
        else:
            if sorted([word1.count(i) for i in set(word1)])== sorted([word2.count(i) for i in set(word2)]):
                return True
            else: return False
"""
Time complexity O(nlogn)
Space complexity O(n)
"""

# Approach 2
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        ref1, ref2 = {}, {}
        for char in word1:
            ref1[char] = ref1.get(char, 0) + 1
        for char in word2:
            ref2[char] = ref2.get(char, 0) + 1
        if sorted(ref1.values()) == sorted(ref2.values()) and sorted(ref1.keys()) == sorted(ref2.keys()):
            return True
        else: return False
"""
Here the solution works by checking the count of keys and values are same for both the words each time.
Time complexity O(nlogn)
Space complexity O(n)
"""
