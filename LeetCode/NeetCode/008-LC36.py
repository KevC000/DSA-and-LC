#Valid Sudoku

from ast import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in cols[c] or 
                board[r][c] in rows[r] or 
                board[r][c] in squares[(r//3 , c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
    
# Time O(N^2), Space O(N)
# Check each element on the board to see if it already exists in the row the column and the 3x3 square area.
# We map all the rows and columns and squares as a key to the hashmap map and the elements to the set as the element at the location.
# If not, not add it in the row, col and square.
# If we check throough the whole thing without an invalid placement of a element we return True