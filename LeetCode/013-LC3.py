#Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequency = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            right_c =  s[r]
            frequency[right_c] = 1 + frequency.get(right_c, 0)
            while frequency[right_c] > 1:
                left_c = s[l]
                frequency[left_c]-=1
                l+=1
            longest = max(longest,r-l+1)
        return longest 

                
# Time: O(N) Space: O(1)/O(N)
# We can solve this suing 1 nested loop(O(N^2)) and a hashmap/hashset, but to optimize we can use 2 pointers.
# The two pointers represent the start and end of the substring and we use a hashmap to record the current substrings frequency.
# When a letter grows beyond a frequency of 1 we start incrementing and removing from the left pointer until we have all unique values in the susbtring.
# When we know we have all unique values we update the longest susbtring variable if needed.
            
