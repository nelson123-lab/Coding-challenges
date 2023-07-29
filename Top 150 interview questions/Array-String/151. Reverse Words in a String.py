class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()
        return " ".join(string[::-1])

"""
Time Complexity O(n)
- The split() method takes O(n) time complexity, the reversing also takes O(n) time Complexity. When combined O(n)
Space Complexity O(n)
- Here when split happens the list formed uses space according to the input size.
"""
