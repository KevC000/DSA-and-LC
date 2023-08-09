# Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        res.append(newInterval)
        return res

# Time: O(N) Space: O(N)
# We iterate through the intervals and compare the end of the new interval with the start of the current interval.
# If the end of the new interval is less than the start of the current interval, we append the new interval to the result and return the result.
# If the start of the new interval is greater than the end of the current interval, we append the current interval to the result.
# If the intervals overlap, we update the new interval to be the union of the two intervals.
# If we can insert the new interval, we return the result.
# Merge Intervals
