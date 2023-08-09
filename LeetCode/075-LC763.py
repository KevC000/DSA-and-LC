# Partition Labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_appearance = {}
        for i,c in enumerate(s):
            last_appearance[c] = i
        
        start = 0
        char_with_latest = s[0]
        for i,c in enumerate(s):
            if last_appearance[c] > last_appearance[char_with_latest]:
                char_with_latest =  c
            if  i == last_appearance[char_with_latest]:
                res.append(i-start+1)
                start = i+1
        return res 

# Time: O(N) Space: O(N)
# We use a dictionary to store the last appearance of each character.
# We iterate through the string and update the last appearance of the character.
# We use a variable to store the starting index of the current partition.
# We use a variable to store the character with the latest last appearance.
# If the last appearance of the current character is greater than the last appearance of the character with the latest last appearance, we update the character with the latest last appearance.
# If the index is equal to the last appearance of the character with the latest last appearance, we append the length of the current partition to the result and update the starting index of the current partition.
# If we can partition the string, we return the result.
