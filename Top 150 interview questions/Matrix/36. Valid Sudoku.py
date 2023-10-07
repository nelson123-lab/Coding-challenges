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

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Creating row, column and 3x3 subgrids.
        row, col, cell = [0]*9, [0]*9, [0]*9
        # Iterating through all the possible i, j possibilities for a sudoko.
        for i, j in product(range(9), repeat= 2):
            # Checking if the cell is empty
            if board[i][j] != '.':
                # Creating a mask
                mask = 1 << int(board[i][j])-1
                # Finding in which subgrid this particular i, j cell is present.
                """
                eg: i, j = (5,1)  will result in c value = 3, 3rd subgrid.
                """
                c = (i//3)*3 + j//3
                if mask&row[i] or mask&col[j] or mask&cell[c]:
                    return False
                row[i] |= mask
                col[j] |= mask
                cell[c] |= mask
        return True
"""
```
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
```

Let's focus on the cell at row `0` and column `1`, which contains the number `3`.

1. `board[0][1]` gives us the value of the cell at row `0` and column `1`, which is `"3"`.

2. `int(board[0][1])` converts the string `"3"` to an integer, giving us the value `3`.

3. `int(board[0][1])-1` subtracts `1` from `3`, resulting in `2`.

4. `1 << int(board[0][1])-1` performs a bitwise left shift operation. The number `1` is shifted to the left by `2` positions.

   In binary representation, `1` is `0001`. Shifting it to the left by `2` positions gives us `0100`, which is `4` in decimal representation.

   So, the value of `mask` becomes `4`.

In this example, the line of code `mask = 1 << int(board[i][j])-1` sets `mask` to `4`, representing the presence of the number `3` in the Sudoku board.

Time Complexity O(n^2) but it simplifies to O(1) since the value of n is constant doesn't depend on the input.
Space Complexity O(n) but it simpleifies to O(1) since the value of n is 9. It doesn't change according to the input. 
"""
