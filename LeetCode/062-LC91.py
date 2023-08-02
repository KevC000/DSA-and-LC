# Decode Ways
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if(i+1 < len(s)
                and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')
            ):
                res += dfs(i+2)
            dp[i] = res
            return res 
        
        return dfs(0)

# Time: O(n) Space: O(n)
# We use recursion to find the number of ways to decode the string.
# We use a dictionary to store the number of ways to decode the string from a particular index.
# We check if the current element is 0, if yes, we return 0.
# We check if the current element and the next element form a valid number, if yes, we add the number of ways to decode the string from the next index to the current index.
# We return the number of ways to decode the string from the current index.