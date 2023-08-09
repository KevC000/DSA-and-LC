# Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            new_interval = intervals[i]
            while i+1 < len(intervals) and new_interval[1] >= intervals[i+1][0]:
                new_interval = [min(intervals[i+1][0], new_interval[0]), max(intervals[i+1][1], new_interval[1])]
                i+=1
            res.append(new_interval)
            i+=1
        return res
    
# Time: O(NlogN) Space: O(N)
# We sort the intervals.
# We iterate through the intervals and compare the end of the current interval with the start of the next interval.
# If the end of the current interval is greater than or equal to the start of the next interval, we update the current interval to be the union of the two intervals.
# If the intervals do not overlap, we append the current interval to the result.
# If we can merge the intervals, we return the result.
# 