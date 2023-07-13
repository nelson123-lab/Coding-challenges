class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        rows = {}

        for r in range(n):
            row = tuple(grid[r])
            rows[row]= 1 + rows.get(row, 0)
        
        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            count += rows.get(col, 0)
            
        return count

"""

1. The `equalPairs` function takes a 2D grid as input and returns the count of equal pairs.

2. The variable `n` is assigned the length of the grid, which represents the number of rows or columns in the square grid.

3. The variable `count` is initialized to 0. This will be used to keep track of the count of equal pairs.

4. The dictionary `rows` is created to store the frequency of each row in the grid. The keys of the dictionary are tuples representing the rows, and the values are the count of occurrences of each row.

5. The first loop iterates over each row in the grid. For each row, it converts the row into a tuple using `tuple(grid[r])`. This is done because lists are not hashable and cannot be used as dictionary keys, but tuples can. The `rows` dictionary is then updated to increment the count of the current row.

6. The second loop iterates over each column in the grid. For each column, it creates a tuple by extracting the elements from each row at the current column index using a list comprehension. The `count` variable is incremented by the value associated with the current column tuple in the `rows` dictionary. If the column tuple is not present in the `rows` dictionary, it defaults to 0.

7. Finally, the `count` variable is returned, which represents the total count of equal pairs in the grid.

This code efficiently counts the number of equal pairs in the grid by utilizing a dictionary to store the frequency of rows and then using that information to count the equal pairs in the columns.
"""
