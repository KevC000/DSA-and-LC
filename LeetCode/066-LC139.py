# Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
    
# Time: O(n^2) Space: O(n)
# We use dynamic programming to find if the string can be broken into words from the dictionary.
# We use a list to store if the string can be broken into words from the dictionary from a particular index.
# We set the last element of the list to True.
# We iterate over the list from the second last element to the first element.
# We iterate over the words in the dictionary.
# We check if the current index + the length of the current word is less than or equal to the length of the string and the substring from the current index to the current index + the length of the current word is equal to the current word.
# We set the current element of the list to the element of the list at the index of the current index + the length of the current word.
# We return the first element of the list.