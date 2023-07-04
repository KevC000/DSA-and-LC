#Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

# Time O(N) Space O(N)
# We want to perform the operations on the most recent 2 numbers which we can keep track of with a stack.
# Iterate through the tokens, if it is an operator we perform the operations on the top 2 items in the stack and append the result which where we will perform more operations as we iterate throught the tokens.
# If we have a number we append that to the stack to be used later.