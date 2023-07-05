#Search in Rotated Sorted Array
from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

# Thought process:   
# Time : O(logN) Space: O(1)
# We can search in linear time but if we use a modified version of binary search we can find in logN time
# How should we modify binary search?
# We also consider if the we in the first portion or the second of the unpivoted version of the array by looking ar nums[-1]
# Then we move if target is less than mid or not, or if target is less than l if we are in the first unpivoted half or greater than r if we are in the second pivoted half
