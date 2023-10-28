import itertools

class Solution:
    def find_combinations(self, lists):
        if len(lists) == 1:
            return list(itertools.product(*lists))
        elif len(lists) == 2:
            combinations = []
            for combination in itertools.product(*lists):
                combinations.append("".join(combination))
        else:
            combinations = []
            for combination in itertools.product(lists[0], self.find_combinations(lists[1:])):
                combinations.append("".join(combination))
        return combinations

    def letterCombinations(self, digits: str) -> List[str]:
        numdir = {"1": "", "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9":["w", "x", "y", "z"]}
        len_digits = len(digits)
        if len_digits == 0:
            return []
        elif len_digits == 1:
            return numdir[digits]
        else:
            digit_list = [numdir[char] for char in list(digits)]
            output = self.find_combinations(digit_list)
        return output

"""
Time complexity O(3^n)
Space Completely O(3^n)
"""

# Easier solution

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d = ["", "","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n = len(digits)
        a = []
        def solve(i,s):
            if len(s)==n:
                a.append("".join(s))
            if i==n:
                return
            for j in range(len(d[int(digits[i])])):
                s.append(d[int(digits[i])][j])
                solve(i+1,s)
                s.pop()
                solve(i+1,s)
            return 
        solve(0,[])
        return a


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [i for i in d[digits[0]]]
        arr = Solution.letterCombinations(self, digits[1:])
        ans = []
        for j in d[digits[0]]:
            for i in arr:   
                ans.append(j+i)
        return ans
