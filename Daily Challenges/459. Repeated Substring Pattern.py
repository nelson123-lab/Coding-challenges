class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        end = 1
        while end < length//2 + 1:
            substring = s[0:end]
            lengthSub = len(substring)
            if length % lengthSub == 0:
                coefficient = length// lengthSub
                if substring*coefficient == s:
                    return True
                else:
                    end += 1
            else:
                end += 1
        return False

"""
Time Complexity O(n^2)
- Here the time complexity is due to the extra O(n) time complexity for comparing strings within the while loop
Space Complexity O(n)
- Here the space complexity is due to the substring we are using for storing the substrings.
"""

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
