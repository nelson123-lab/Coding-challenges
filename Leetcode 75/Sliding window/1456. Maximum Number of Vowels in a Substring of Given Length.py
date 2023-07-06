class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        window = s[:k]
        def v_count(array):
            count = 0
            for i in array:
                if i in vowels:
                    count += 1
                else: pass
            return count

        maxCount = currCount = v_count(window)
    
        for i in range(k, len(s)):
            window = s[i-k+1:i] + s[i]
            currCount = v_count(window)
            maxCount = max(currCount, maxCount)

        return maxCount

a = Solution()
print(a.maxVowels("abciiidef", 3))

