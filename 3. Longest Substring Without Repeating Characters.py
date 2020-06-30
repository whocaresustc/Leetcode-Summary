# O(n) O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                 start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length

    # O(n) O(n)
    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            used = {}
            max_length = left = 0
            for right, c in enumerate(s):
                if c in used and left <= used[c]:
                    left = used[c] + 1
                else:
                    max_length = max(max_length, right - left + 1)

                used[c] = right

            return max_length