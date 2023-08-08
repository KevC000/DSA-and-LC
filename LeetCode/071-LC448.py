# Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            j = abs(nums[i])-1
            nums[j] = abs(nums[j])*-1
        for i in range(1,n+1):
            if nums[i-1] > 0:
                res.append(i)
        return res 
    
# Time: O(n) Space: O(1)
# We iterate through the array and mark the index of the value at the current index as negative.
# We iterate through the array again and append the index of the positive values to the result.
# We return the result.
