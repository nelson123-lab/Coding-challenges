class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                sub = ""
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * sub)
        return "".join(stack)

"""
We won't be able to use no = int(stack.pop()) because the number won't always be 1 digit. 
for example "100[leetcode]" 
- In this case we have to make the num as a string then only we will be able to get the 100 as the coefficient of mulitplication.

Time Complexity O(n)
- Only 1 iteration is happening. The while operations are of constant time and the worst case in O(n). Thus the total time complexity is O(n).
Space COmpelxity O(n)
- The space complexity is due to the stack used. The maximum space can depend on the input string.
"""
