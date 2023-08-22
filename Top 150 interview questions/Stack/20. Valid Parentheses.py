class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"{": "}", "[": "]", "(": ")"}

        brackets_array = [bracket for bracket in s]

        for b in brackets_array:

            if b in '([{':
                stack.append(b)
            elif b in '}])':
                if not stack:
                    return False
                last_bracket = stack[-1]
                if dictionary[last_bracket] == b:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
