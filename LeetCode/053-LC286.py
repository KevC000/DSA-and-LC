# Walls and Gates
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = distance

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if min(row, col) < 0 or row == ROWS or col == COLS:
                        continue
                    if (row, col) in visited or rooms[row][col] == -1:
                        continue
                    visited.add((row, col))
                    q.append([row, col])

            distance += 1

# Time: O(MN) Space: O(MN)
# We use BFS to find the distance of each empty room from the nearest gate.
# We start with all the gates in the queue and then we keep on adding the adjacent empty rooms to the queue and mark them as visited.
# We keep on doing this until there are no more empty rooms left.
# If there are no more empty rooms left, we return the distance of each empty room from the nearest gate.
