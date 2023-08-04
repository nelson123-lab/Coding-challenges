class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p, q = 0, 0 # represents the pointers for s and t respectively.
        if len(s) > len(t):
            return False

        while p < len(s) and q < len(t):
            if s[p] == t[q]: # Checking for same characters existence in both the strings.
                p += 1
            q += 1
        return p == len(s) # Checking if all the characters of s has been iterated.

"""
The algorithm uses two pointer approach with two pointers iterating through each of the strings. 
Time Complexity O(n)
- Here n is the length of the longer string.
Space Complexity O(1)
"""
