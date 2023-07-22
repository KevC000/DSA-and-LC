#Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited =set()
        def backtrack(i,r,c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited:
                return False
            if board[r][c] != word[i]:
                return False
            visited.add((r,c))
            res = (backtrack(i+1,r+1,c) or 
            backtrack(i+1,r-1,c) or
            backtrack(i+1,r,c+1) or
            backtrack(i+1,r,c-1)
            )
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0,r,c): 
                    return True
        return False
    
#