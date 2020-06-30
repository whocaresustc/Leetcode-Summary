"""https://leetcode.com/problems/string-transforms-into-another-string/discuss/355412/Python-simple-O(n)-with-explanation"""


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        m = {}
        for i in range(len(str1)):
            if str1[i] not in m:
                m[str1[i]] = str2[i]
            elif m[str1[i]] != str2[i]:
                return False
        return len(set(str2)) < 26