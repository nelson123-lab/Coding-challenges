class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def pat(s):
            res = []
            c = {}
            for v in s:
                if v not in c:
                    c[v] = len(c)
            for i in s:
                res.append(c[i])
            return res
        pattern = pat(pattern)
        ans = []
        for word in words:
            if pat(word) == pattern:
                ans.append(word)
        return ans
        
