
# O(n) O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.is_Palindrome(s[l + 1:r + 1]) or self.is_Palindrome(s[l:r])

        return True # don't forget return True here

    def is_Palindrome(self, s):
        return s == s[::-1]