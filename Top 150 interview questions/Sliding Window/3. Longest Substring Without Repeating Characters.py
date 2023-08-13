class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        char_map = {}
        max_len = 0
        while right < len(s):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

"""
Time complexity O(n)
- Here it uses a while loop along with a Hashmap so the overall the time complexity is only O(n)
Space Complexity O(min(n,m))
- Where m is no of unique characters present in the string. n is the total number of characters, when the entire characters within in the string is unique the space required will be O(n).
"""
