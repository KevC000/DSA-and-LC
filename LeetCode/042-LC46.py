#Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n =  nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res += perms
            nums.append(n)
        return res
        
# Time: O(N!) Space: O(1)
# We start with getting the permutations of a portion of the array with the first element appended to the end for all it's permutations.
# Add that result to the higher result.
