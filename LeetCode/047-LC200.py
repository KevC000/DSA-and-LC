# Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == "0" or grid[r][c] == "-1":
                return

            grid[r][c] = "-1"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count+=1
                    dfs(r,c)

        return count
    
# Time: O(N*M) Space: O(N*M)
# Iterate through the grid and if we find a 1 we increment the count and call dfs on it
# In the dfs we check if we are out of bounds or if we are on a 0 or -1 and return
# Otherwise we set the current cell to -1 and call dfs on the 4 directions
# We do this to avoid visiting the same cell twice