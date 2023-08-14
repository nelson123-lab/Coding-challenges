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
- Here there is only 1 iteration happening. The time complexity of searching a characters in a set is only O(1).
Space Complexity O(n)
- Here a hashmap is used to store the data. The maximum number of characters stored will be n.
"""
