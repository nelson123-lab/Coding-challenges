class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        else:
            return (s+s)[1:len(s)*2-1].find(s)!=-1

"""
Time Complexity O(n)
Space Complexity O(n)
"""

"""
KMP algorithm to compute the Longest Proper Prefix
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = self.computeLPS(s)
        return lps[n-1] != 0 and n % (n - lps[n-1]) == 0

    def computeLPS(self, s: str) -> List[int]:
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

        return lps
"""
Time Complexity O(n)
Space Complexity O(1)
"""
