class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board[0])
        n = len(board)

        for x in range(m):
            board[0][x] *= 10
        for y in range(n):
            board[y][0] *= 10
        
        for y in range(n):
            for x in range(m):
                neighbors = board[y][x] % 10
                if y != n - 1 and x != m - 1:
                    board[y + 1][x + 1] *= 10
                alive = board[y][x] >= 10
                for x2, y2 in ((x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)):
                    if x2 < 0 or x2 == m or y2 == n:
                        continue
                    if board[y2][x2] >= 10:
                        neighbors += 1
                    if alive:
                        board[y2][x2] += 1
                if neighbors == 3 or (alive and neighbors == 2):
                    board[y][x] = 1
                else:
                    board[y][x] = 0
                
        return board
