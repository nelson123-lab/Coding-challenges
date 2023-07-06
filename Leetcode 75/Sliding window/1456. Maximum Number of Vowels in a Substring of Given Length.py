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

"""
The above solution exceeded the time limit so we need to optimize the areas where it uses more time. I think I need to remove the 
function part and count the number of vowels in a simple way.
"""

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
"""
Here instead of checking vowels count each time by counting through the entire list. We can check whether the removed element was a vowel and the newly added 
element was a vowel
"""
        for i in range(k, len(s)):
            window = s[i-k+1:i] + s[i]
            if s[i-k] in vowels:
                currCount -= 1
            if s[i] in vowels:
                currCount += 1
            maxCount = max(currCount, maxCount)

        return maxCount
