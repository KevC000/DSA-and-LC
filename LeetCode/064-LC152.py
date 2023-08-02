# Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        currMin, currMax = 1, 1
        for n in nums:
            temp = currMax * n
            currMax = max(temp, currMin*n, n)
            currMin = min(temp, n * currMin, n)
            max_product = max(max_product, currMax)
            
        return max_product
    
# Time: O(n) Space: O(1)
# We use dynamic programming to find the maximum product subarray.
# We use two variables to store the current minimum and maximum product.
# We set the current minimum and maximum product to 1.
# We iterate over the array.
# We set a temporary variable to the current maximum product times the current element.
# We set the current maximum product to the maximum of the temporary variable, the current minimum product times the current element, and the current element.
# We set the current minimum product to the minimum of the temporary variable, the current minimum product times the current element, and the current element.
# We set the maximum product to the maximum of the maximum product and the current maximum product.
# We return the maximum product.