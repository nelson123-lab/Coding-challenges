class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Get a 2D Array
        elementLst = []
        for row in range(len(board)):   # Row
            for col in range(len(board[row])):   # Entry in row
                if board[row][col] != ".":
                    elementLst.append((board[row][col], row, col))
        
        # Check cases in 2D array
        for i in range(len(elementLst)):
            for j in range(len(elementLst)):
                if elementLst[i][0] == elementLst[j][0] and i != j:
                    if elementLst[i][1] == elementLst[j][1]:
                        return False
                    if elementLst[i][2] == elementLst[j][2]:
                        return False
                    if elementLst[i][1] // 3 == elementLst[j][1] // 3 and elementLst[i][2] // 3 == elementLst[j][2] // 3:
                        return False
        return True

"""
Time Complexity O(n^2)
Space Complexity O(n)
"""
