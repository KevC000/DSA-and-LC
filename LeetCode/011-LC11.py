# Container With Most Water

from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height)-1

        while l < r:
            left = height[l]
            right = height[r]
            curr_height = min(left, right)
            area =  curr_height*(r-l)
            max_area = max(max_area, area)
            if left>=right:r-=1 
            else: l+=1
                
        return max_area
    
# Time O(N) Space O(1)
# The height of the area of water will be the minimum of the elements at start and end of the container which we can represent as two pointers
# The width will be the distance between the two pointers.
# To maximize the distance we set the pointers are the start and end of the array. 
# Then we decrement the left and right pointers depending on which is lower since we water to maximize the height we want the greater height between the two.
# We keep checking the max area and the current area until the two pointers meet.