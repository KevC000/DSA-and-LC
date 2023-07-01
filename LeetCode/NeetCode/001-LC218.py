#Contains Duplicate

from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for num in nums:
            if num in vals:
                return True
            vals.add(num)
        return False
# Use a set to record elements that have already been visited.
# If it already exists we have duplicates as it already exists.
# Otherwise we keep iterating and adding elements to the set until we find a duplicate or visited the entire array, in which case return False.
# Time: O(N) We may have to viist entire array
# Space: O(N) We may have to add the entire array to the set.