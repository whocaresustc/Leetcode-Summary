from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, len(p) - 1
        res = []
        counter_p = Counter(p)
        counter_s = Counter(s[:right])
        for right in range(len(p) - 1, len(s)):
            counter_s[s[right]] += 1
            if counter_s == counter_p:
                res.append(left)

            # update left
            counter_s[s[left]] -= 1
            if counter_s[s[left]] == 0:
                del counter_s[s[left]]
            left += 1

        return res