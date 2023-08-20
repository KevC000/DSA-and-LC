# Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s)-1

        while l < r:
            if s[l] != s[r]:
                return self.is_palindrome(s, l+1,r) or self.is_palindrome(s, l, r-1)
            l+=1
            r-=1
        return True

    def is_palindrome(self, s , l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    
# Time: O(N) Space: O(1)
# We use a two pointer approach. We iterate through the string and check if the characters at the left and right pointers are equal. If they are not, we check if the string is a palindrome if we remove the character at the left pointer or the character at the right pointer. If it is, we return True. Otherwise, we return False.
# We return True if we have not returned False.
#