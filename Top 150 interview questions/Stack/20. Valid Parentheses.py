class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(': ')', '{': '}', '[' :']'}

        brackets = list(s)
        for b in brackets:
            if b in '({[':
                stack.append(b)
            elif b in ']})':
                if not stack:
                    return False
                lastBracket = stack[-1]
                if dict[lastBracket] == b:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
"""
Time Complexity O(n^2)
- Here the O(n) time complexity is due to the opeartion of " if b in '({['. It works within a for loop. Which results in overall time compelxity of O(n^2)
Space Complexity O(n)
- The space compelxity is due to the bracket list that is created according to the input. The stack list can also contribute to the space complexity but it's mainly due to the bracket list.
"""

"""
The above solution can be optimized to O(n) time compelxity by making some modifications.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(': ')', '{': '}', '[' :']'}
        brackets = list(s)
        setA = set('({[')
        setB = set(']})')
        for b in brackets:
            if b in setA:
                stack.append(b)
            elif b in setB:
                if not stack:
                    return False
                lastBracket = stack[-1]
                if dict[lastBracket] == b:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

"""
Time Complexity O(n)
- Here the time complexity reduced to O(n) since checking whether an element exists in set is an O(1) operation.
Space Complexity O(n)
- The space complexity is same as above.
"""
