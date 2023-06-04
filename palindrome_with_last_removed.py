def validPalindrome(s: str) -> bool:
    a, b = s[:-1], s[1:]
    if s[::-1] == s:
        return True
    elif a[::-1] == a or b[::-1] == b:
        return True
    else:
        for i in range(1, len(s[1:-1])+1):
            left, right = i, len(s)-i-1
            new_char = ""
            # convert string to list
            s_list = list(s)

            # replace character at index
            s_list[left] = new_char

            # convert list back to string
            new_s = "".join(s_list)
            if new_s[::-1] == new_s:
                return True
            s_list = list(s)
            s_list[right] = new_char
            new_s = "".join(s_list)
            if new_s[::-1] == new_s:
                return True
        return False

print(validPalindrome("eddze"))

# This solution exceeds the time limit it can be solved by using two - pointer approach.

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
