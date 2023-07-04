#Permutation In String

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq = {}
        s1_map = Counter(s1)
        for r in range(len(s2)):
            curr_r = s2[r]
            freq[curr_r] = 1 + freq.get(curr_r,0)
            while r-l+1 > len(s1):
                curr_l = s2[l]
                freq[curr_l] -= 1
                if freq[curr_l] == 0: del freq[curr_l]
                l+=1
            if freq == s1_map: return True
        return False

# Time O(N) Space O(N)
# We can check if s1 is a permutation of s2 if we have equal hashmaps within a substring of s2. 
# We use a sliding window and hashmap to keep track of the substring, and maintain fixed size of len(s1).