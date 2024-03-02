# Solution using Two pointer approach
class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s_list = list(s)
        vowels = ['a', 'e','i','o','u']
        while l<r:
            if s_list[l].lower() not in vowels:
                l += 1
            if s_list[r].lower() not in vowels:
                r -= 1
            if s_list[l].lower() in vowels and s_list[r].lower() in vowels:
                temp = s_list[l]
                s_list[l] = s_list[r]
                s_list[r] = temp
                l += 1
                r -= 1
        return "".join(s_list)
"""
Time Complexity O(n2)
Space Complexity O(n)
"""

# Solution using an empty string and a different approach.
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        v = []
        for i in range(len(s)):
            if s[i] in vowels: v.append(s[i])
            else: pass

        v = v[::-1]
        v_c = 0
        for i in range(len(s)):
            if s[i] not in vowels: res += s[i]
            else: 
                res += v[v_c]
                v_c += 1
        return res

"""
Time Complexity O(n), it uses a set instead of a list so search operation within a list is O(1)
Space Complexity O(n)
"""

# Solution with Inplace update
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        v = []
        for i in range(len(s)):
            if s[i] in vowels:
                v.append(s[i])
            else: pass
        v = v[::-1]
        v_c = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + v[v_c] + s[i+1:]
                v_c += 1
        return s

"""
Time Complexity O(n)
Space Complexity O(n)
"""
