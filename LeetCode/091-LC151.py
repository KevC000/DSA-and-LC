# reverse words in string

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = []

        i = 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1

            curr = ''
            while i < len(s) and s[i] != ' ':
                curr += s[i]
                i += 1
            if curr:
                s_list.append(curr)

        return ' '.join(s_list[::-1])

# Time: O(N) Space: O(N)
# We iterate through the string and add the words to a list
# We then reverse the list and join the words with spaces.
# We return the string.
