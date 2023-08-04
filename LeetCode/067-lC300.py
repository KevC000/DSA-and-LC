# Longest Increasing Sequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1 for i in range(len(nums))]
        max_increasing = 1
        for i in range(len(nums)):
            curr = 0
            for j in range(i):
                if nums[j] < nums[i]:
                     if cache[j] > curr:
                         curr = cache[j]
            cache[i] = curr+1
            max_increasing = max(max_increasing, cache[i])
        return max_increasing

# Time: O(n^2) Space: O(n)
# We use dynamic programming to find the length of the longest increasing subsequence.
# We use a list to store the length of the longest increasing subsequence from a particular index.
# We set the first element of the list to 1.
# We iterate over the list from the second element to the last element.
# We iterate over the elements in the list from the first element to the current element.
# We check if the current element is greater than the element at the current index.
# We check if the element at the current index is greater than the current element.
# We set the current element of the list to the maximum of the current element of the list and the element at the current index of the list + 1.
# We return the maximum element of the list.