class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

"""
This is a simple problem. It returns the last words length. In python, if you index lst[-1] it will return the last element.
Time Complexity O(n)
- The split method uses O(n) time complexity to make the split.
Space COmplexity O(1)
- No space that is depended on the input is used.
"""
