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

"""
The above solution can be optimized for faster operation.
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(columnNumber % 26 + ord('A')) + ans
            columnNumber //= 26
        
        return ans
"""
Time Complexity O(1)
- Here the time complexity is reduced to O(1)
Space Complexity O(log(columnNumber))
- The space complexity remains the same.
"""


