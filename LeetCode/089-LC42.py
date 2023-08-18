# Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]

        cmax = 0
        for i in range(len(left)):
            temp = max(cmax, height[i])
            left[i] = cmax
            cmax = temp

        cmax = 0
        for i in range(len(right)-1,-1,-1):
            temp = max(cmax, height[i])
            right[i] = cmax
            cmax = temp
        print(left)
        print(right)
        res = 0
        for i in range(1, len(height)-1):
           ceil = min(left[i],right[i])
           if ceil - height[i] > 0:
               res+= ceil - height[i]
        
        return res 
# Time: O(N) Space: O(N)
# We create two arrays left and right which will store the maximum height to the left and right of the current index.
# We iterate through the array and store the maximum height to the left of the current index.
# We iterate through the heights and find the minimum of the left and right maximum height.
# If the minimum is greater than the current height, we are able to trap water and add to the result.
# We return the total amount of water trapped.