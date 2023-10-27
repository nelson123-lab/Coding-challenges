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
        
