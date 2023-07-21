class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)

        for i in range(l):
            for j in range(i, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(l):
            matrix[i] = matrix[i][::-1]
        return matrix
        
