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

# Approach 3 Easier to understand and efficient
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def vowels_c(vow):
            count = 0
            for char in vow:
                if char in vowels:
                    count += 1
            return count

        substring = s[:k]
        initial_count = vowels_c(substring)
        maxV = max(0, initial_count)

        for i in range(len(s)-k):
            if substring[0] in vowels:
                initial_count -= 1
            if s[k+i] in vowels:
                initial_count += 1

            substring = substring[1:] + s[k+i]
            maxV = max(maxV, initial_count)
        return maxV

"""
- Here we are first identifying the no of vowels in the substring and then checking for no of substring count in each window by adding and substracting count depeding on whether vowels are added or not.
Time Complexity O(n)
Space COmplexity O(1)
"""
