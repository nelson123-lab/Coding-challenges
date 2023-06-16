class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_index = -1
        for idx, ele in enumerate(s):

            if ele in t and t.index(ele) > prev_index:
                prev_index = t.index(ele)
            else:
                return False
        return True

def isSubsequence(self, s: str, t: str) -> bool:
    i, j  = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)

ans = Solution()
print(ans.isSubsequence(s ="acb", t ="ahbgdc"))