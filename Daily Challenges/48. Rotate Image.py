class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 2-part problem

        # 1) figure out how to translate cell values correctly
            # newRow = oldCol
            # newCol = n - 1 - oldRow
        
        # 2) figure out how to iterate over the square properly, such that values are not overridden and lost
            # we should iterate over each group of 4 partner-cells, before moving to the next set
            # to do this, we should iterate over one quadrant, and find each of the 4 partners based on that quadrant

        
        # fqbr (first quadrant bounds row) is the bounds of the first quadrant
        fqbr = n // 2 - 1 if n % 2 == 0 else n // 2
        fqbc = n // 2 - 1

        for row in range(fqbr + 1):
            for col in range (fqbc + 1):

                a = (row, col)
                b = (col, n - 1 - row)
                c = (n - 1 - row, n - 1 - col)
                d = (n - 1 - col, row)

                temp = matrix[a[0]][a[1]]
                matrix[a[0]][a[1]] = matrix[d[0]][d[1]]
                matrix[d[0]][d[1]] = matrix[c[0]][c[1]]
                matrix[c[0]][c[1]] = matrix[b[0]][b[1]]
                matrix[b[0]][b[1]] = temp



