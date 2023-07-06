#Generate Parenthesis

from ast import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open, close):
            if open == close == n:
                res.append(''.join(stack))
                return
            if open < n:
                stack.append('(')
                backtrack(open+1, close)
                stack.pop()
            if close < open:
                stack.append(')')
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return res
    
# Time O(2^N)? Not sure, as the number of parenthesis increases the possibilities double I assume? Space: O(N)

# We look for each possibility using backtracking. When building a possible result we can have multiple open parenthesis and end up with a valid result.
# However if we have more closing parenthesis we can not have a possible end result since need matching closing for every ending.
# So we exclude any possible answers when we add more closing parenthesises to the result. 