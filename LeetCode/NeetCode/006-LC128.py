#Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        length = 0
        unique =  set(nums)

        for n in nums:
            curr = n
            if curr-1 not in unique:
                while curr in unique:
                    length+=1
                    longest = max(longest,length)
                    curr+=1
                length=0    
        return longest
    
# Time O(N) Space O(N)    
# We use a set to check if a number is in the list O(1) Time
# We check each element(n) to see if the there is n+1 in the set and keep updating the current length and max length
# An edge case to keep in mind is if a large part of the list is consectutive already, so we check if n-1 already exists before checkign for consecutives.