# Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_all = sum(nums)
        if sum_all % 2 != 0:
            return False
        target = sum_all//2

        values = set()
        values.add(0)

        for i, n in enumerate(nums):
            for value in list(values):
                if (n+value) == target:
                    return True
                values.add(n)
                values.add(n+value)
        return False

# Time: O(n^2) Space: O(n)
# We use dynamic programming to find if the array can be partitioned into two subsets with equal sum.
# We use a set to store the sum of the elements in the array.
# 
                