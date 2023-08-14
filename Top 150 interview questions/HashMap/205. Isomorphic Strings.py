class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        p = set()
        for i in range(len(s)):
            x, y = s[i], t[i]
            if x in d:
                if d[x] != y:
                    return False
            else:
                if y in p:
                    return False
                d[x] = y
                p.add(y)
        return True

"""
Time Complexity O(n)
Space Complexity O(n)
"""
