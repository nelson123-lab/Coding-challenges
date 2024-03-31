class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return

            for char in mappings[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations

"""
- The backtrack function recursive backtracking algorithm that generates all possible combinations of letters.
- The backtrack function takes two parameters: index and path.
    index keeps track of the current position in the digits string.
    path keeps track of the current combination of letters being formed.

Time Complexity: O(4 n)
Space Complexity: O(4 n)
"""
