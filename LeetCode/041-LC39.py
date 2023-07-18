#Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def createSum(i, curr_addends, curr_sum):
            if curr_sum == target:
                res.append(curr_addends.copy())
                return
            if i >= len(candidates) or curr_sum > target:
                return

            curr_addends.append(candidates[i])
            createSum(i, curr_addends, curr_sum+candidates[i])

            curr_addends.pop()
            createSum(i+1, curr_addends, curr_sum)


        createSum(0, [], 0)
        return res
    
# Time: O(len(candidates ^ (candidates/smallest_candite))) Space: O(target/smallest_candidate)
# We check each possibility by either adding the current candidate or move on to the next.
# If it equals the sum we add the current addends to the resulting array and return.
# If it i goes out of range or we exceeded the target we return.