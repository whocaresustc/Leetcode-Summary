# sliding window

"""If a string have occurrences x times,
any of its substring must appear at least x times.

There must be a substring of length minSize, that has the most occurrences.
So that we just need to count the occurrences of all substring with length minSize.
"""


# Similar to problem 159. Longest Substring with At Most Two Distinct Characters
# The difference is that this problem is a fixed window, when move right pointer, left pointer has to be updated
# While 159 is not a fixed-window, right pointer will keep move until doesn't satisfy condition and then move the left pointer



from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        candidate = Counter(s[:minSize - 1])
        ans = {}

        for right in range(minSize - 1, len(s)):
            char = s[right]
            candidate[char] += 1

            if len(candidate.keys()) <= maxLetters:
                ans[s[left:right + 1]] = ans.get(s[left:right + 1], 0) + 1

            # update left
            candidate[s[left]] -= 1  # s[left] not left
            if candidate[s[left]] == 0:
                del candidate[s[left]]
            left += 1

        return max(ans.values()) if ans else 0  # for example 4 case


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        ans = {}
        candidate = {}

        for right in range(len(s)):
            char = s[right]
            candidate[char] = candidate.get(char, 0) + 1

            if right >= minSize - 1:  # only when meet the minimum size window

                if len(candidate.keys()) <= maxLetters:
                    ans[s[left:right + 1]] = ans.get(s[left:right + 1], 0) + 1

                # update left
                candidate[s[left]] -= 1  # s[left] not left
                if candidate[s[left]] == 0:
                    del candidate[s[left]]
                left += 1

        return max(ans.values()) if ans else 0  # for example 4 case