class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2): return False
        else:
            if sorted([word1.count(i) for i in set(word1)])== sorted([word2.count(i) for i in set(word2)]):
                return True
            else: return False
