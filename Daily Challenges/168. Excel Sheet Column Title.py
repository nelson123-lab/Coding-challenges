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
