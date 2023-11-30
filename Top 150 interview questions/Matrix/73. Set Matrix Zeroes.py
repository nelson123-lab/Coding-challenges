class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = set()
        # setZeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zeros.add((i,j))
        for x,y in zeros:
            for k in range(len(matrix[0])):
                matrix[x][k] = 0
            for l in range(len(matrix)):
                matrix[l][y] = 0
                
