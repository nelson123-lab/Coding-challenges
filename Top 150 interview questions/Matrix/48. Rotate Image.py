class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = [list(i) for i in list(zip(*matrix))]
        res = []
        for i in temp:
            res.append(i[::-1])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = res[i][j]

"""
TIme Complexity O(n^2)
Space Complexity O(n^2)
"""
