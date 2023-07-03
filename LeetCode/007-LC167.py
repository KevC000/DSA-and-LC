#Input Array Is Sorted

from ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 ,len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1, r+1]

# Time: O(N) Space O(1)
# Left and right pointer at the start and end of the array
# We know it's in asceding order so we can decrement or increment depending if the sum of those two is greater or less than the target
# We return L+1 and R+1 since it is 1-indexed.