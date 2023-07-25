# Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        time = 0       
        q = deque()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh_oranges > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(len(grid)) 
                    and col in range(len(grid[0])) 
                    and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh_oranges-=1
            time+=1
                
        return time if fresh_oranges == 0 else -1
# Time: O(MN) Space: O(MN)
# We use BFS to find the time taken for all the oranges to rot.
# We start with all the rotten oranges in the queue and then we keep on adding the adjacent fresh oranges to the queue and mark them as rotten.
# We keep on doing this until there are no more fresh oranges left.
# If there are no more fresh oranges left, we return the time taken for all the oranges to rot.
# If there are still fresh oranges left, we return -1.