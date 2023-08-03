class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()
        return new == new[::-1]

"""
Time Complexity is O(n)
- It's because the .isalnum() works in O(1) time complexity. It uses bitmap character classification table to check whether the string contains all characters or not.
Space Complexity is O(n)
- Space is used according to the input size in the variable new.
"""
