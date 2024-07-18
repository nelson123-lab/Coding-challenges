# Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

"""
- Here we only need to check if the sorted of both the strings is equal.
Time Compelxity O(nlogn)
Space Complexity O(n)
"""

# Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref1 = {}
        ref2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            ref1[i] = ref1.get(i, 0) + 1
        for i in t:
            ref2[i] = ref2.get(i, 0) + 1
        if ref1 == ref2:
            return True
        else: return False

"""
- Here we are using two hashmaps to keep track of the element count in the s and t. This reduces the time complexity for sorting.
Time complexity O(n)
Space complexity O(n)
"""
