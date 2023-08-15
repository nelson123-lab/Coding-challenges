class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

"""
The main idea is the anagram is valid only if the characters in s and t are same. 
Time Complexity O(n log n)
- Each of the strings are sorted, the worst case scenario of sorting is O(n log n).
Space Complexity O(n)
- It takes n spaces as the length of the string.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
This is a more optimal solution which works in O(n) time complexity.
Time Complexity O(n)
- Since we use hashmap to determine the valid anagrams.
Space Complexity O(n)
- Here it takes the length of characters as the space.
"""
