# Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res^=n
        return res
# Time: O(N) Space: O(1)
# Count: we iterate through the nums array.
# We XOR the result with the current number.
# We return the result.