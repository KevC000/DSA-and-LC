# Palindrome Partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            l, r = 0, len(s)-1
            while r > l:
                if s[r] != s[l]:
                    return False
                r -= 1
                l += 1
            return True

        def buildPartition(i, curr):
            if i == len(s):
                all_palindromes = True
                for substring in curr:
                    if not isPalindrome(substring):
                        all_palindromes = False
                if all_palindromes:
                    res.append(curr.copy())
                    return
                else:
                    return
            curr.append(s[i])
            buildPartition(i+1, curr)

            curr.pop()
            if curr:
                curr[-1] = curr[-1]+s[i]
                buildPartition(i+1, curr)

        buildPartition(0, [])
        return res

# Time: O(N*2^N) Space: O(N)
# Check all possibilities of substrings. Either add the current char to the last substring or create a new substring in the current array
# If all letters are a palindrome then we append to the resulting list.
