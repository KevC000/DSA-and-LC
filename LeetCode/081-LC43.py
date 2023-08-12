# Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mapping = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
        }
        res = 0
        outer_digit = 1
        for i in range(len(num1)-1,-1,-1):
            n1 = num1[i]
            inner_digit = 1
            curr = 0
            for j in range(len(num2)-1,-1,-1):
                n2=num2[j]
                curr += mapping[n1]*mapping[n2]*inner_digit
                inner_digit*=10
            res+=curr*outer_digit 
            outer_digit *= 10
        return str(res) 

# Time: O(MN) Space: O(1)
# We iterate through the first number from right to left.
# We iterate through the second number from right to left.
# We calculate the product of the two numbers and add it to the result.
# We return the result.
# 