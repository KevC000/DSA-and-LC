# Group Anagrams

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return anagrams.values()
    
# O(NM) time O(NM) space    
# We are given a list of strings, and we want to output a nested array grouped by anagrams
# We iterate through the input array and map the anagrams
# We check if it's an anagram by sorting however it will increase time complexity 
# So to optimized we use an array of numbers that represent the count of the letter and the index represent the order in the alphabet.
# Then we return the values of the map.