class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        output = []

        # while len(output) < rows * cols: This while condition could also be used since we know the expected length of output
        while top < bottom and left < right:
            #Print top row, left to right
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            #Print right column, top to bottom
            for i in range(top, bottom):
                output.append(matrix[i][right - 1])
            right -= 1

            #Print bottom row, right to left
                #This loop has a subtle problem if we've already printed the last row on line 14!
                #Basically, if we've printed the last row in the middle of the matrix up above, we haven't updated left variable, we only updated top
                #which might cause part of that row to get printed again in this loop
            #To solve the above problem, we also check the top variable to make sure the same row doesn't get printed twice
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    output.append(matrix[bottom - 1][i])
                bottom -= 1

            #Print left column, bottom to top
                #This loop also has a subtle problem similar to what was described above
            #Get around this problem by comparing left and right beforehand
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
        
        return output

"""
Time Complexity O(n*m)
Space Complexity O(n)
"""
