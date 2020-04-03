# O(n**2) O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ret_1 = self.expand_around_center(s, i, i)
            ret_2 = self.expand_around_center(s, i, i + 1)
            if len(ret_1) > len(ans):
                ans = ret_1
            if len(ret_2) > len(ans):
                ans = ret_2
        return ans

    def expand_around_center(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[(left + 1):right]
