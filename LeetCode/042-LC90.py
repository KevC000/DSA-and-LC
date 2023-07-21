#Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def getSubsets(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            getSubsets(i+1, curr)
            curr.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            getSubsets(i+1, curr)
        
        getSubsets(0,[])
        return res

# Time: O (N*2^N) Space: O(N*2^N)
# Same as subsets(LC078) except we skip all duplicated after getting possibilities witht that number.
