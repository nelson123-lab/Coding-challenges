class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            temp = columnNumber % 26
            if temp == 0:
                temp = 26
                columnNumber -= 26
            c = chr(ord('A') + temp - 1)
            ans = c + ans
            columnNumber //= 26
        return ans

"""
Time Complexity O(log(columnNumber)
- Here logarithmic time complexity is present for the algorithm since the loop iterates until it becomes zero.

Space complexity O(log(columnNumber)
- The space is also logarithmic since the ans variable is dependent on the input.
"""


