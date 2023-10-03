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

