class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, float(-inf))
            dfs(len(heights)-1, c, atlantic, float(-inf))
        for r in range(ROWS):
            dfs(r, 0, pacific, float(-inf))
            dfs(r, len(heights[0])-1, atlantic, float(-inf))

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
# Time: O(MN) Space: O(MN)
# Top most row and the left most column are connected to the Pacific Ocean and the bottom most row and right most column are connected to the Atlantic Ocean.
# So we perform DFS from the top most row and left most column and mark all the cells that can be reached from the Pacific Ocean.
# So we perform DFS from the bottom most row and right most column and mark all the cells that can be reached from the Atlantic Ocean.
# We mark them in two different sets and then we find the intersection of the two sets.
# The cells that are present in both the sets are the cells that can be reached from both the oceans.