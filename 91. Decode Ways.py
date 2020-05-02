# O(N) O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0]= 1
        dp[1] = 1 if s[0] != '0' else 0 # attention
        for i in range(2, len(s) + 1):
                dp[i] = (s[i-1] != '0') * dp[i-1] + (int(s[i-2:i]) in range(10, 27)) * dp[i-2]  # last digit and last two digit
        return dp[-1]

    # O(N) O(1)
    class Solution:
        def numDecodings(self, s: str) -> int:
            a = 1
            b = c = 1 if s[0] != '0' else 0  # attention

            for i in range(2, len(s) + 1):
                c = (s[i - 1] != '0') * b + (int(s[i - 2:i]) in range(10, 27)) * a  # last digit and last two digit
                a, b = b, c
            return c