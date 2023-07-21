#Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curr, target):
            if target == 0:
                res.append(curr.copy())
                return
            if target <= 0:
                return
            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev: 
                    continue
                curr.append(candidates[i])
                backtrack(i+1, curr, target-candidates[i])
                curr.pop()
                prev = candidates[i]
        backtrack(0, [], target)
        return res
    
# Time: O(2^N) Space: O(N)
# Iterate through the list and recursively call the fuction with the current while updating curr and target
# If it equals target update the resulting list. If we exceeded the target we return
# Remove the current number and contiue iterating with the rest of the numbers