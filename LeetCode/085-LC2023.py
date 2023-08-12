# Detect Squares
class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] +=1

    def count(self, point: List[int]) -> int:
        res = 0
        qx,qy = point
    
        for (px,py), n in self.points.items():
            dx, dy = abs(qx-px), abs(qy-py)
            if dx == dy and dx > 0:
                c1 = (qx, py)
                c2 = (px, qy)
                if c1 in self.points and c2 in self.points:
                    res += n*self.points[c1]*self.points[c2]
        return res


# Time: O(N) Space: O(N)
# Count: we deconstruct the point argument
# We iterate through the points dictionary.
# We deconstruct the key into px and py.
# We calculate the dx and dy (distance).
# if the dx and dy are equal and greater than 0, we have a square.
# we look up the points of the other two corners of the square.
# if they exist, we add the product of the three points to the result.
# reiterate throught the other points.
# return the result.