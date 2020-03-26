# if s = "110001111000000", then groups = [2, 3, 4, 6]

# O(N) O(N)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0
        for i in range(len(groups) - 1):
            ans += min(groups[i], groups[i + 1])
        return ans


# O(N) O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return ans



