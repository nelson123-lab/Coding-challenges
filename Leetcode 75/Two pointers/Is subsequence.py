class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_index = -1
        for idx, ele in enumerate(s):

            if ele in t and t.index(ele) > prev_index:
                prev_index = idx
            else:
                return False
        return True
    
ans = Solution()
print(ans.isSubsequence(s ="acb", t ="ahbgdc"))