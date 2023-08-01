# Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
        return count

#Time: O(n^2) Space: O(1)
# We use two pointers to find palindromic substrings.
# We check if the current element is a palindrome and update the count.
# Then we expand the palindrome by checking the adjacent elements.
# We do the same for the even length palindromes.
# We return the count.
         