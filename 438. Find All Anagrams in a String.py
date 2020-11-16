from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = 0
        ans = []

        Counter_p = Counter(p)
        Counter_s = Counter()

        for R in range(len(s)):
            Counter_s[s[R]] += 1

            if R >= len(p) - 1:
                if Counter_s == Counter_p:
                    ans.append(L)

                # Update left
                Counter_s[s[L]] -= 1
                if Counter_s[s[L]] == 0:
                    del Counter_s[s[L]]
                L += 1

        return ans