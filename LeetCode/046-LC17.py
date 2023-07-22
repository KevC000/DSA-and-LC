#Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_mapping ={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []

        def generate_possibilities(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            digit = digits[i]
            letters = digits_mapping[digit]

            for letter in letters:
                generate_possibilities(i+1,curr+letter)
        
        if digits:
            generate_possibilities(0,"")

        return res

# Time O(N*4^N) Space O(N)
# For each possible letter of that number we recursivly call the function with the remaining letters mapping.
# When the length of the current string reaches the length of the digits string we add that possibility to the resulting array.
