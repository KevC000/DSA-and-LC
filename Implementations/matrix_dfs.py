def dfs(grid,r,c,visited):
    rows, cols = len(grid), len(grid[0])
    if r == rows or c == cols or (r,c) in visited or min(r,c) < 0:
        return
    
    visited.add((r,c))
    
    dfs(grid, r+1,c)
    dfs(grid, r-1,c)
    dfs(grid, r,c+1)
    dfs(grid, r,c-1)
    
    visited.remove((r,c))