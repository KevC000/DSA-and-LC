# Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        return goal == 0
# Time: O(n) Space: O(1)
# We start from the end of the array and keep track of the goal.
# If the current index + the value at the current index is greater than or equal to the goal, we update the goal.
# We return True if the goal is 0, else False.
