from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque((0,0))
    visited = set()
    set.add((0,0))
    
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for nr,nc in neighbors:
                if r+nr == ROWS and c+nc == COLS and min(r,c) < 0 or (r+nr, c+nc) in visited:
                    continue
                q.append((r+nr,c+nc))
                visited.add((r+nr,c+nc))
                    
            