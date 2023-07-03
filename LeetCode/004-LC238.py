#Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]

        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= product
            product *= nums[i]
        return res

# Time: O(N) Space: O(1)
# Create a resulting list equal to the length of the original array
# Iterate starting from the start of the orginal and the resulting array and replace the resulting array witht he running product before the element at the index.
# Do it no starting from the end of the arrays.
 
