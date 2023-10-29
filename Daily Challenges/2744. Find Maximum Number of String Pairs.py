class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        l = len(words)
        for i in range(l):
            for j in range(i+1,l):
                if words[i] == words[j][::-1]:
                    cnt+=1

        return cnt            
