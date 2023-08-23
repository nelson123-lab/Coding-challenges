# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         alphabet_dict = {}
#         for i in range(ord('A'), ord('Z')+1):
#             alphabet_dict[i - ord('A') + 1] = chr(i)
#         if columnNumber == 1:
#             return alphabet_dict[columnNumber]
#         else:
#             total = 0
#             for i in columnNumber:
#                 total += alphabet_dict[i]
#             return total
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber:
            tmp = columnNumber % 26
            if tmp == 0:
                tmp = 26  # chr(26) is Z
                columnNumber -= 26

            c = chr(ord('A') + tmp - 1)            
            ans = c + ans

            columnNumber //= 26

        return ans
