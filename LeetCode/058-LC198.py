# House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_profit = 0
        
        for i in range(len(nums)):
            max_previous = 0
            for j in range(i-1):
                max_previous = max(max_previous, nums[j])
            nums[i] = nums[i] + max_previous
            max_profit = max(max_profit, nums[i])

        return max_profit
    

# Time: O(n^2) Space: O(1)
# We use DP to find the maximum profit.
# We iterate over the array and for each element we find the maximum profit we can get from the previous elements.
# We add the current element to the maximum profit and update the maximum profit.

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_previous, max_profit = 0, 0

        for n in nums:
            temp = max(max_previous+n, max_profit)
            max_previous = max_profit
            max_profit = temp
            
        return max_profit

# Time: O(n) Space: O(1)
# We use DP to find the maximum profit.
# We iterate over the array and for each element we find the maximum profit we can get from the previous elements.
# We add the current element to the maximum profit and update the maximum profit.
# We use two variables to store the maximum profit from the previous elements and the maximum profit.
# We update the maximum profit from the previous elements and the maximum profit for each element.
# We return the maximum profit.

 

