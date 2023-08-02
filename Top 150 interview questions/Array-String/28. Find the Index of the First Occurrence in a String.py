class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i:i+ len(needle)] == needle:
                return i
        return -1

"""
Time Complexity O(n) where n is the length of the needle.
Space Complexity O(1)
"""
