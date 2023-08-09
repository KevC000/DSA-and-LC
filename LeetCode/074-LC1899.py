# Merge Triplets to Form Target Triplet
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        can_use = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, val in enumerate(t):
                if val == target[i]:
                    can_use.add(i)
        
        return len(can_use) == 3
# Time: O(N) Space: O(1)
# We use a set to store the indices of the triplets that can be used.
# We iterate through the triplets and check if we can use them.
# If we can, we add the indices to the set.
# If the length of the set is 3, we return True.
