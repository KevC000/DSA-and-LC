# Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 0
        while r < (len(nums)-1):
            max_jump = 0
            for i in range(l, r+1):
                max_jump = max(max_jump, i+nums[i])
            l = r+1
            r = max_jump
            count += 1
        return count
    
# Time: O(n^2) Space: O(1)
# We keep track of the left and right bounds of the current jump.
# We iterate through the current jump and find the maximum jump we can make.
# We update the left and right bounds of the next jump and increment the count.
# We return the count.
