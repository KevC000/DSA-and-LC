# Daily Temperatures
from ast import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                stack_day = stack.pop()
                res[stack_day] =  day - stack_day
            stack.append(day)
        return res
                
# Time: O(N) Space: O(N)
# Create a resulting arr equal to the length of the temperatures and teh default value is 0
# We can iterate through the temperature and use the stack to respresent the most recent days
# We push the index to the stack and when we can retrieve the temperature using that index too.
# When we've reached a day where the current temperature is greater than the top of the stack we set the result for that day.
# The result for that day will be the differenve between the current day and index in that stack which represents the day.
# We keep iterating through the stack until there are no more days that is less than the current day or until we have no more items in the stack.
