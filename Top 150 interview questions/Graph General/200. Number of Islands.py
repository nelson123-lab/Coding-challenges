from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        # retrieve the bounds
        n_rows, n_cols = len(grid), len(grid[0])
        islands = 0
        # visit each cell
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1' and grid[i][j] != -1:
                    # do the DFS here
                    q = deque([(i, j)])
                    grid[i][j] = -1
                    while q:
                        row, col = q.popleft()
                        # try visit all valid directions
                        for dr, dc in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                            r, c = row + dr, col + dc
                            if (r >= 0 and r < n_rows and c >= 0 and c < n_cols 
                                and grid[r][c] == '1'):
                                q.append((r, c))
                                grid[r][c] = -1
                    # increment the number of connected islands
                    islands += 1
        return islands

"""
- The problem can be done using BFS and DFS.
Time Complexity O(N*M)
Space Complexity O(N*M)
- The space used by the queue.
"""
