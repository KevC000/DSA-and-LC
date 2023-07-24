# Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited or min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            return 1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        return max_area
# Time: O(N*M) Space: O(N*M)
# Iterate through the grid and if we find a 1 we call dfs on it and update the max area
# In the dfs we check if we are out of bounds or if we are on a 0 or if we have visited the cell
# and return 0
# Otherwise we add the current cell to the visited set and call dfs on the 4 directions
# We do this to avoid visiting the same cell twice

