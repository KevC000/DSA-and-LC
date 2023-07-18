#Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def get_subsets(i, current_set):

            if i >= len(nums):
                subsets.append(current_set.copy())
                return
                
            current_set.append(nums[i])
            get_subsets(i+1, current_set)
            current_set.pop()
            get_subsets(i+1, current_set)

        get_subsets(0,[])
        return subsets
    
# Time: O(N*2^N) Space: 2^N
# For each number in the list we can either decide to include that in the subset or not
# We build each possibiliy with and without that number for each number.