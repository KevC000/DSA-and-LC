#Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Time O(N) Space O(N)
# Create a reversed sorted array as pairs of position an speed. Sort by reversed position.
# This simulates the start postion of cars.
# Use the stack to simulate the movement of the cars. We calculate the time it takes for the car to reach the target.
# If it the times it takes is longer than the number below it then it becomes a fleets to indicate it has become a  fleet we remove it.
# Keep repeating until we've iterated throught the pairs array.
# the length of the stack is the number of fleets.

