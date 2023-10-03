class Solution:
    def _pattern(self, s):
        lookup, output = {}, []
        i = 0
        for c in s:
            if c in lookup:
                output.append(lookup[c])
            else:
                i += 1
                lookup[c] = i
                output.append(i)
        return output

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = self._pattern(pattern)
        output = []
        for word in words:
            if self._pattern(word) == p:
                output.append(word)
            else: pass
        return output
        
"""
- Here we are making a new method for the class. You can write it as a function within the findAndReplacePattern function too.
- The idea here is that we are converting our pattern to a integer format such that when a similar pattern word appears it will also return the same pattern.
- Let's see with an example. 

'abb' -> [1, 2, 2] # pattern
'mqq' -> [1, 2, 2] # word, the charaters can be replaced to obtain the pattern.
'abc' -> [1, 2, 3] # Here replacing all similar character with a different character won't give us the output. 

Time Complexity O(n*m)
Space Complexity O(n*m)
"""

"""
Below is the second approach that saves more space.
"""
class Solution:
    def pattern_check(self, s, p):
        d1, d2 = {}, {}
        for a, b in zip(s, p):
            if a not in d1: d1[a] = b
            if b not in d2: d2[b] = a

            if a!= d2[b] or b!= d1[a]:
                return False
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            if self.pattern_check(word, pattern):
                output.append(word)
            else: pass
        return output
"""
Here we are using two hashmaps to keep track of the pattern and mapping the word and the pattern together and if the same character is not mapping to the same character later within the word leads to an False result.

Time complexity: O(N*M)
Space complexity: O(M)
- Here the space is used only for storing the pattern within the dictionary. The output list is not considered as extra space since the problem requires us to output like that.
"""
