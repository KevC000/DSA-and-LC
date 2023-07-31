# House Robber 2

class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_robbed(houses):
            max_previous, max_profit = 0, 0

            for profit in houses:
                new_max = max(max_previous+profit, max_profit)
                max_previous = max_profit
                max_profit = new_max
            return max_profit

        return max(nums[0],max_robbed(nums[1:]), max_robbed(nums[:-1]))
    
# Time: O(n) Space: O(1)
# We use DP to find the maximum profit.
# We iterate over the array and for each element we find the maximum profit we can get from the previous elements.
# We add the current element to the maximum profit and update the maximum profit.
# We use two variables to store the maximum profit from the previous elements and the maximum profit.
# We update the maximum profit from the previous elements and the maximum profit for each element.
# We return the maximum profit.
# We also check if we can get the maximum profit by robbing the first house or the last house.
# We return the maximum profit.