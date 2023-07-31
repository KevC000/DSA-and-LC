#  Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > res_r-res_l+1:
                    res_l=l
                    res_r=r
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > res_r-res_l+1:
                    res_l=l
                    res_r=r
                l-=1
                r+=1
        return s[res_l:res_r+1]
    
#Time: O(n^2) Space: O(1)
# We use two pointers to find the longest palindromic substring.
# We check if the current element is a palindrome and update the longest palindromic substring.
# Then we expand the palindrome by checking the adjacent elements.
# We do the same for the even length palindromes.
# We return the longest palindromic substring.