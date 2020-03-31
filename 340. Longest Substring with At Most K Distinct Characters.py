# Sliding window + hashmap
# O(n) O(k)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        start = 0
        visited = {}
        ans = 0
        for end in range(len(s)):
            visited[s[end]] = visited.get(s[end], 0) + 1
            while start <= end and len(visited) > k:
                visited[s[start]] -= 1
                if visited[s[start]] == 0:
                    del visited[s[start]]
                start += 1
            ans = max(ans, end - start + 1)
        return ans

# Better Sliding window + hashmap: not general method
# O(n) O(k)
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {} # key is the unique character, value is the max index for each character
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]] # after deleting, len(d) == k
                low += 1
            ret = max(i - low + 1, ret)
        return ret