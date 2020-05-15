class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l + 1 < r:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        if isBadVersion(l):
            return l
        if isBadVersion(r):
            return r
        return -1