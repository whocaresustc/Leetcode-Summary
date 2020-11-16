# O(len(s) + len(t))   O(len(t))
# Check 3. Longest Substring Without Repeating Characters
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target = Counter(t)
        right = 0
        res = ""
        matched = 0
        minlength = float("inf")
        for left in range(len(s) - len(t) + 1):
            # Move right until find a solution or reach the end
            while right < len(s) and matched < len(target):
                if s[right] in target:
                    target[s[right]] -= 1  # negative meaning extra characters in t
                    if target[s[right]] == 0:
                        matched += 1
                right += 1  # right move one more position than the matched substring

            # update result
            if matched == len(target):
                if right - left < minlength:
                    minlength = right - left
                    res = s[left:right]

            # update left
            if s[left] in target:
                target[s[left]] += 1  # target is dynamic if left is excluded, then target is updated to reflect the change
                if target[s[left]] > 0:
                    matched -= 1

        return res


# More straightforward to template
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target = Counter(t)
        left = 0
        res = ""
        matched = 0
        minlength = float("inf")
        for right in range(len(s)):
            if s[right] in target:
                target[s[right]] -= 1  # negative meaning extra characters in t
                if target[s[right]] == 0:
                    matched += 1

            while left <= right and matched == len(target):  # <= not < for case "a" "a"
                if right - left < minlength:
                    minlength = right - left
                    res = s[left:right + 1]

                    # update left
                if s[left] in target:
                    target[s[left]] += 1
                    if target[s[left]] > 0:
                        matched -= 1
                left += 1  # no matter s[left] in or not in target, always move it
        return res