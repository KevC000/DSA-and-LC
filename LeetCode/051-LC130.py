# Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS =  len(board), len(board[0])
        def mark_as_unsurrounded(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = 'U'
            mark_as_unsurrounded(r+1,c)
            mark_as_unsurrounded(r-1,c)
            mark_as_unsurrounded(r,c+1)
            mark_as_unsurrounded(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and board[r][c] == 'O':
                    mark_as_unsurrounded(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'U':
                    board[r][c] = 'O'
                    
# Time: O(MN) Space: O(MN)
# We mark all the cells that are connected to the boundary as 'U' 
# and then we mark all the cells that are not connected to the boundary as 'X'.
# Then we mark all the cells that are marked as 'U' as 'O' and all the cells that are marked as 'O' as 'X'.