class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()

        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        res = []

        while len(seen) != len(matrix[0]) * len(matrix):
            # go right, boundary is left and right
            p = left
            while p <= right and len(seen) != len(matrix[0]) * len(matrix):
                res.append(matrix[top][p])
                seen.add((top, p))
                p += 1
            top += 1 # we don't return to the top row

            # go down, boundaries is top and bottom
            p = top
            while p <= bottom and len(seen) != len(matrix[0]) * len(matrix):
                res.append(matrix[p][right])
                seen.add((p, right))
                p += 1
            right -= 1 # we don't return to this right row

            # go left
            p = right
            while p >= left and len(seen) != len(matrix[0]) * len(matrix):
                res.append(matrix[bottom][p])
                seen.add((bottom, p))
                p -= 1
            bottom -= 1 # we don't return to the top

            # go up, boundaries are top and bottom
            p = bottom
            while p >= top and len(seen) != len(matrix[0]) * len(matrix):
                res.append(matrix[p][left])
                seen.add((p, left))
                p -= 1
            left += 1
            
        return res
            
