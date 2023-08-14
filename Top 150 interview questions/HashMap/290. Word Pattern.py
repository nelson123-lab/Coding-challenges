class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = s.split(" ")
        if len(pattern) != len(pattern_map):
            return False
        d = {}
        p = set()
        for i in range(len(pattern)):
            a, b = pattern[i], pattern_map[i]
            if a in d:
                if d[a] != b:
                    return False
            else:
                if b in p:
                    return False
                else:
                    d[a] = b
                    p.add(b)
        return True

"""
The main edge case in the problem is to check whether different character maps to same character. That's why we keep the set p to keep track of the newer characters corresponding values. If it gets repeated it will return 
False.
Time Complexity O(n)
- Here the time complexity is O(n). The split method takes O(n) time complexity to split the data.
Space Complexity O(n)
- Here the space complexity is O(n). The dictionary uses n space when n is the length of the string pattern.

"""
