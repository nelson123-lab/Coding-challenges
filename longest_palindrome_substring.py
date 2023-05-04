def longestPalindrome(self, string1: str) -> str:
        if string1 == "" or string1 == len(string1) *string1[0]:
            return string1
        
        p = string1[0]
        l = 1
        for i in range(len(string1)):
            for j in range(len(string1), 0, -1):
                str = string1[i:j]
                if str == str[::-1] and len(str) > l:
                    p = str
                    l = len(str)
        return p
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        le = 0
        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > le:
                    res = s[l:r+1]
                    le = r-l+1
                l -= 1
                r += 1
            # Even length
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > le:
                    res = s[l:r+1]
                    le = r-l+1
                l -= 1
                r += 1
        return res

a = Solution()
print(a.longestPalindrome("aabcddsageee"))