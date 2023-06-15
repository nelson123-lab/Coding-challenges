class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split()
        l, r = 0, len(s_list) - 1
        while l < r:
            if s_list[l] == "":
                s_list.pop(l)
                l += 1
            elif s_list[r] == "":
                s_list.pop(r)
                r -= 1
            else:
                l += 1
                r -= 1
        return " ".join(s_list[::-1]).strip()

ans = Solution()
print(ans.reverseWords("  hello world  "))

# This was waste of time. 
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        words.reverse()
        return " ".join(words)
