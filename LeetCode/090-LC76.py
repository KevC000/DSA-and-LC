# Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''

        t_map = Counter(t)
        sub_map = {}

        start = 0
        res_start = -1
        res_end = len(s)
        matches_needed = len(t_map)
        matches = 0

        for end in range(len(s)):
            curr = s[end]
            if curr in t_map:
                sub_map[curr] = 1 + sub_map.get(curr, 0)
                if sub_map[curr] == t_map[curr]:
                    matches+=1
            while matches == matches_needed:
                if end-start+1 < res_end-res_start+1:
                    res_start = start 
                    res_end = end
                if s[start] in sub_map:
                    sub_map[s[start]]-=1
                    if sub_map[s[start]] < t_map[s[start]]:
                        matches-=1
                start+=1
        return s[res_start: res_end+1] if res_start != -1 else ''
         
# Time: O(N+M) Space: O(M) M is the length of t
# We use a sliding window approach. We keep track of the number of matches we need to find in the string.
# We also keep track of the number of matches we have found in the string.
# We keep track of the start and end of the substring that contains all the characters in t.
# We iterate through the string and add the characters to a map. If the character is in t and the number of times it appears in the substring is equal to the number of times it appears in t, we increment the number of matches.
# If the number of matches is equal to the number of matches needed, we have found a substring that contains all the characters in t. We then check if the length of the substring is less than the length of the current substring. If it is, we update the start and end of the substring.
# We then remove the character at the start of the substring from the map. If the character is in t and the number of times it appears in the substring is less than the number of times it appears in t, we decrement the number of matches.
# We then increment the start of the substring.
# We return the substring if we have found a substring that contains all the characters in t. Otherwise, we return an empty string.
