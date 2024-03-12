class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_index = -1
        for idx, ele in enumerate(s):

            if ele in t and t.index(ele) > prev_index:
                prev_index = t.index(ele)
            else:
                return False
        return True
# The above solution makes the test case true. 


# The below is a working solution using two pointer approach.
# def isSubsequence(self, s: str, t: str) -> bool:
#     i, j  = 0, 0

#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
    
#     return i == len(s)

ans = Solution()
print(ans.isSubsequence(s ="ab", t ="baab"))

# Two pointer appraoch
class Solution(object):
    def isSubsequence(self, s, t):``
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_p = 0 # s_p to track characters in string s
        t_p = 0 # t_p to track characters in string t.
        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1
        return s_p == len(s)

"""
- Uses two pointers to keep track of the characters of the strings s and t.
- Then it tracks for the same character, and if the order fails, the value of s_p will not match the length of the subsequence string s if it is a subsequence.
Time Complexity O(n)
Space Complexity O(1)
"""
